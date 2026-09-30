class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(min_to_search, curr_sum, curr_list):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_list.copy())
            
            # Otherwise we still need to add an element
            next_min_to_search = min_to_search
            for num in nums[min_to_search:]:
                curr_sum += num
                curr_list.append(num)
                backtrack(next_min_to_search, curr_sum, curr_list)
                
                next_min_to_search += 1
                curr_list.pop()
                curr_sum -= num
                
                
            
        backtrack(0, 0, [])
        return res
