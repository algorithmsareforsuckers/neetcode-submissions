"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals: return True
        std = sorted(intervals, key = lambda x:x.start)
        prev_y = std[0].end
        for inter in std[1:]:
            s = inter.start
            if prev_y > s:
                return False
            prev_y = inter.end
        
        return True