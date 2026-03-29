class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans, l, r = 0, 0, len(heights)-1
        while l < r:
            water = (r-l) * min(heights[l], heights[r])
            ans = max(ans, water)
            print("left: " + str(l) +", height_l: " + str(heights[l]) + ", right: " + str(r) + ", height_r: "+ str(heights[r]) + ", volume: " + str(water))

            if heights[l] > heights[r]:
                r-=1
                print("r-1")
            else:
                l+=1
                print("l+1")
                
            print("Current Max: " + str(ans))
        return ans