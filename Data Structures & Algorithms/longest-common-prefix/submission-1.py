class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(0, len(strs[0])):
            i+=1
            curr_prefix = strs[0][:i]
            for s in strs:
                if s[:i] != curr_prefix:
                    return ans
            ans = curr_prefix
        return ans
