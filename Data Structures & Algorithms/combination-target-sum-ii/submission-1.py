class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def backtrack(start_ind, curr_sum, curr_list):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            
            si = start_ind
            for i in range(start_ind, len(candidates)):
                si += 1
                # Add next to list and curr sum
                if i > start_ind and candidates[i-1] == candidates[i]:
                    continue
                curr_sum += candidates[i]
                curr_list.append(candidates[i])
                backtrack(si, curr_sum, curr_list)

                # Remove
                curr_sum -= candidates[i]
                curr_list.pop()
        
        backtrack(0, 0, [])
        return res