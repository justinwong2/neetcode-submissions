class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        #currently can have overlapping
        stack = []
        for i in range(len(intervals) - 1, -1, -1):
            stack.append(intervals[i])
        ans = []
        while stack:
            currInterval = stack.pop()
            if len(stack) == 0:
                ans.append(currInterval)
                continue
            nextInterval = stack[-1]
            #if the next one is completely smaller, pop it and only add mine
            if currInterval[0] <= nextInterval[0] and currInterval[1] >= nextInterval[1]:
                stack.pop()
                stack.append(currInterval)
            #since it is ascending, i just need to check the right side?
            elif currInterval[1] >= nextInterval[0] and currInterval[1] <= nextInterval[1]:
                currInterval[1] = nextInterval[1]
                stack.pop()
                stack.append(currInterval)
            elif currInterval[1] < nextInterval[0]:
                ans.append(currInterval)
        return ans
        