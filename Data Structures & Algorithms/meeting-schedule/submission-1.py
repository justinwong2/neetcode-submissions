"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda x: x.start)
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            if prevInterval.end > currInterval.start:
                return False
            prevInterval = currInterval
        return True
