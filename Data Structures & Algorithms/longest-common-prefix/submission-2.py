class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for n in range(len(strs[0])):
            c = strs[0][n]
            for s in strs:
                if not s or len(s) <= n or s[n] != c:
                    return prefix
            prefix = prefix + c
        return prefix