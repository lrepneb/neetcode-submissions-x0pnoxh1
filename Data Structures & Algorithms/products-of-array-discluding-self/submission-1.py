class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [1] * nums_len
        pre=post=1
        for n in range(nums_len):
            ans[n] = pre
            pre*=nums[n]
        
        for n in range(nums_len):
            ans[nums_len-n-1] *= post
            post*=nums[nums_len-n-1]
        return ans