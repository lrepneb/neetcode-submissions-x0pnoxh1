class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {}

        for ind, val in enumerate(nums):
            ids[val] = ind
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in ids and ids[diff] != ind:
                return [ind, ids[diff]]