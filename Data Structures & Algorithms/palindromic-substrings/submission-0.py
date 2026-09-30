class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def bfs(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                right += 1
                left -= 1
                count += 1
            
            return count
            
        for i, c in enumerate(s):
            odd = bfs(i, i)
            even = bfs(i, i+1)
            res += odd + even
        
        return res
