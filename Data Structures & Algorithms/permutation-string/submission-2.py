class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        cnts = defaultdict(int)
        num_wrong = 0
        for char in s1:
            if cnts[char] == 0:
                num_wrong += 1
            cnts[char] += 1
        
        
        l = 0
        # we will just scan every window of length s1
        for r, char in enumerate(s2):
            print(l, r, s2[l], s2[r], num_wrong)
            cnts[char] -= 1
            if cnts[char] == 0:
                num_wrong -= 1
            if num_wrong == 0:
                return True
            
            if r - l < len(s1) - 1:
                continue

            # updates
            cnts[s2[l]] += 1
            if cnts[s2[l]] == 1:
                num_wrong += 1
            l += 1
            

        return False
