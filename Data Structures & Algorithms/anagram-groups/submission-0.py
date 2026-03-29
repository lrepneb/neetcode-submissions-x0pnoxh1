class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each string, maintain original as double?
        ans = {}
        for s in strs:
            s_sorted = str(sorted(s))
            ans[s_sorted] = ans.get(s_sorted, []) + [s]
        ans = list(ans.values())
        return ans