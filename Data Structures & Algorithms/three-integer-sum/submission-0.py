class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Three pointer: i scrolls | j, k pincer
        ans = []
        nums.sort()

        for i in range(len(nums)):
            target = 0 - nums[i]
            j, k = i+1, len(nums)-1
            while(j<k):
                jk = nums[j] + nums[k]
                if jk > target:
                    k-=1
                elif jk < target:
                    j+=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
        return [list(x) for x in set(tuple(x) for x in ans)]
            