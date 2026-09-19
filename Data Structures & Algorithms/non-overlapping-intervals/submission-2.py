class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        prevInterval = intervals[0]
        removed = 0
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            #if it doesnt overlap, continue
            if prevInterval[1] <= currInterval[0]:
                prevInterval = currInterval
                continue
            #if it eats into it, i will ignore the next one because i sorted it by end timings, means my current one has a shorter end timing, which means it is less likely to overlap with a future start timing
            elif prevInterval[1] > currInterval[0]:
                removed += 1
        
        return removed

        