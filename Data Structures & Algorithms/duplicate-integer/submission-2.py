class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > 1:
                return True
        return False