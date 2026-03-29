class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            to_add = []
            for a in ans:
                if n not in a:
                    print(str(to_add), type(to_add))
                    print(str(a), type(a))
                    print(str(n), type(n))
                    temp = a + [n]
                    to_add.append(temp)
            print("END to_add: " + str(to_add))
            ans = ans + to_add
            print("END ans: " + str(ans))
        return ans