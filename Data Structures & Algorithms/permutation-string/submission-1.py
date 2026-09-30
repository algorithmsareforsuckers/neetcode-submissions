class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        print(len(s1))
        
        counts = defaultdict(int)
        non_zero = 0
        for char in s1:
            if counts[char] == 0:
                non_zero += 1
            counts[char] += 1
        
        l = 0
        for r in range(len(s1)-1):
            counts[s2[r]] -= 1
            if counts[s2[r]] == 0:
                non_zero -= 1


        for r in range(len(s1)-1, len(s2)):
            counts[s2[r]] -= 1
            if counts[s2[r]] == 0:
                non_zero -= 1
            if non_zero == 0:
                return True
            
            if counts[s2[l]] == 0:
                non_zero += 1
            counts[s2[l]] += 1
            l += 1
        
        print(counts)
        return False
            
