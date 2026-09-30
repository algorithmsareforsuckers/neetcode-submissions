from collections import Counter 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0
        i = 0
        while i < len(nums):
            if nums[i]-1 not in counts:
                curr = 1
                k = 1
                while nums[i]+k in counts:
                    curr += 1
                    k += 1
                best = max(best, curr)
            i += 1
            
        return best