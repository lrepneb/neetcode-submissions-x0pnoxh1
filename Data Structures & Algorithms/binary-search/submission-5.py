class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while right-left >= 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1
