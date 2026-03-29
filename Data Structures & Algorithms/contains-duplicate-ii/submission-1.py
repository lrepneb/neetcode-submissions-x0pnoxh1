class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k is the window
        i, j = 0, min(k, len(nums)-1)

        while j < len(nums):
            if len(set(nums[i:j+1])) != len(nums[i:j+1]):
                return True
            else:
                i+=1
                j+=1
        return False