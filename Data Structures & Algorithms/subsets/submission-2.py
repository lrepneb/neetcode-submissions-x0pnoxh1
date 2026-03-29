class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            to_add = []

            for a in ans:
                if n not in a:
                    to_add.append(a + [n])

            ans = ans + to_add
        return ans