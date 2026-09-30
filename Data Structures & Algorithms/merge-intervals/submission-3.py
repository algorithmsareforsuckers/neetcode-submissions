class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mono = sorted(intervals, key = lambda x:x[0]) #monotonic
        res = [mono[0]]

        for start, end in mono:
            last_end = res[-1][1]

            if last_end >= start:
                res[-1][1] = max(res[-1][1], end)
            
            else:
                res.append([start, end])

        return res