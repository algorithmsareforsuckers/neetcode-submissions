class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals, key=lambda x: x[0])

        res = [sort[0]]
        for start, end in sort:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            
            # we are guarenteed that start >= sort[-1][0]
            else:
                res.append([start, end])
        
        return res
