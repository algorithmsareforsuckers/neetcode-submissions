class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, i):
            nonlocal res

            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(curr, i+1)

            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i+1
            
            backtrack(curr, i+1)
            return
        
        backtrack([], 0)
        return res
