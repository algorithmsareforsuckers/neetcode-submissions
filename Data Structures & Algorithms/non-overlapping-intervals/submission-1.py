class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        std = sorted(intervals)

        total = 0
        prev_beg, prev_end = std[0]
        for beg, end in std[1:]:
            if prev_end > beg:
                total += 1
                prev_end = min(prev_end, end)
                continue
            
            prev_end = end
        
        return total

