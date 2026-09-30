class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for n in range(len(strs[0])):
            c = strs[0][n]
            for s in strs:
                if len(s) <= n or s[n] != c:
                    return s[:n]
        return strs[0]