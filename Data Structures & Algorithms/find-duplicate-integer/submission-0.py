class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        for num in nums:
            if seen[num] > 0:
                return num
            seen[num] += 1
        
        return -1