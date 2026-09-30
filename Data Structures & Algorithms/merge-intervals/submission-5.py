class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inc = sorted(intervals, key = lambda x: x[0])
        res = [inc[0]]

        for start, end in inc:
            old_s, old_e = res[-1][0], res[-1][1]

            if old_e >= start:
                res[-1][1] = max(old_e, end)
            else:
                res.append([start, end])
        
        return res