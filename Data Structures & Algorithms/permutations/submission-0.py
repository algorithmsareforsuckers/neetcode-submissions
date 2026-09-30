class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr_list):
            #@print(start_ind, curr_list)
            if len(curr_list) == len(nums):
                res.append(curr_list.copy())
            to_consider = set(nums)
            for elm in curr_list:
                to_consider.discard(elm)


            for num in to_consider:
                print(num, curr_list)
                curr_list.append(num)
                backtrack(curr_list)

                curr_list.pop()
                
            
        
        backtrack([])
        return res