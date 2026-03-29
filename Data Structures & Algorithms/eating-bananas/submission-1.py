class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            
            total_t = 0
            for pile in piles:
                to_add = pile // mid
                if pile / mid > to_add:
                    to_add += 1
                total_t += to_add
            if total_t <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
