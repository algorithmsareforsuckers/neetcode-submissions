class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, i):
            nonlocal res

            if i >= len(nums):
                if sorted(curr) not in res:
                    res.append(sorted(curr).copy())
                return
            curr.append(nums[i])
            backtrack(curr, i+1)

            curr.pop()
            backtrack(curr, i+1)
            
            return
        
        backtrack([], 0)
        return res


            
            