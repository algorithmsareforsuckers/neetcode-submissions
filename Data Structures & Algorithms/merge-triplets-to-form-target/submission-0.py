class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = False
        b = False
        c = False
        for t in triplets:
            if (t[0] == target[0]) and (t[1] <= target[1]) and (t[2] <= target[2]):
                a = True
            if (t[0] <= target[0]) and (t[1] == target[1]) and (t[2] <= target[2]):
                b = True
            if (t[0] <= target[0]) and (t[1] <= target[1]) and (t[2] == target[2]):
                c = True
            
            if a and b and c:
                return True
            
        return a and b and c
        

