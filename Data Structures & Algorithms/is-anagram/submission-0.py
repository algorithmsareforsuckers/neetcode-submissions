class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # okay one approach is make a dict with char counts for first string, then subtract one whenever seen char in t
        if len(s) != len(t):
            # also covers 1 empty case
            return False
        if len(s) == len(t) == 0:
            return True
        
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in t:
            if char in chars:
                chars[char] -= 1
                if chars[char] < 0:
                    return False
            else:
                return False
        
        for val in chars.values():
            if val < 0:
                return False
        
        return True
        