class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = False
        b = False
        c = False
        for t in triplets:
            if (t[0] > target[0]) or (t[1] > target[1]) or (t[2] > target[2]):
                continue

            a = a or (t[0] == target[0])
            b = b or (t[1] == target[1])
            c = c or (t[2] == target[2])
            
            if a and b and c:
                return True
            
        return a and b and c
        

