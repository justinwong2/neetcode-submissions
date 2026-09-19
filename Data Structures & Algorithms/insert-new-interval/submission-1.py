class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = []
        after = []
        isSmaller = 0

        for i in range(len(intervals)):
            currInterval = intervals[i]

            #if my current interval comes completly before my new interval
            if currInterval[1] < newInterval[0]:
                before.append(currInterval)
            #if the new interval is completely smaller then i should keep currInterval and not add the newInterval at the end
            elif currInterval[0] <= newInterval[0] and currInterval[1] >= newInterval[1]:
                isSmaller = 1
                before.append(currInterval)
            #if current interval overlaps on the left side only
            elif currInterval[0] <= newInterval[0] and currInterval[1] <= newInterval[1]:
                newInterval[0] = currInterval[0]
            #if current interval overlaps on the right side only
            elif currInterval[0] <= newInterval[1] and newInterval[1] <= currInterval[1]:
                newInterval[1] = currInterval[1]
            #if the new interval is completely larger i dont add the currInterval
            
            #if my current interval comes completely after my new interval
            elif currInterval[0] > newInterval[1]:
                after.append(currInterval)
        
        if isSmaller == 0:
            before.append(newInterval)
        before.extend(after)
        return before


