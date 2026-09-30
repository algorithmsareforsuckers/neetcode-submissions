import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = [0, float('-inf')]

        for key, val in counts.items():
            if val > best[1]:
                best = [key,val]
        
        return best[0]



        