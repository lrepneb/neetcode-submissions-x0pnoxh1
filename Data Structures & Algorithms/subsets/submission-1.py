class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            to_add = []

            for a in ans:
                if n not in a:
                    temp = a + [n]
                    to_add.append(temp)
                    
            ans = ans + to_add
        return ans