class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False

        n = sum(nums)
        target = n // 2

        if nums[0] == target: return True
        possible = set([nums[0]])
        for i in range(1,len(nums)):
            adds = set()
            if target - nums[i] in possible: return True
            for poss in possible:
                curr = poss + nums[i]
                if curr < target and curr not in possible:
                    adds.add(curr)
            
            for a in adds:
                possible.add(a)
        
        return False


