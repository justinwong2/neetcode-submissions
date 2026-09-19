"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0 or len(intervals) == 1:
            return len(intervals)
        temp = []
        count = 0
        for i in intervals:
            temp.append((i.start, 1))
            temp.append((i.end, -1))
        temp.sort()
        rooms = 0
        answer = 0
        for i in temp:
            rooms += i[1]
            answer = max(answer, rooms)
        return answer

        