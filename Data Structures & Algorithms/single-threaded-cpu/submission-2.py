class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #cpu will choose the shortest processing time
        #if tie break will pick the smallest index
        #enqueue time is when the task will become available
        #i maintain 2 pqs?
        
        import heapq
        pq1 = []
        pq2 = []
        ans = []

        for i in range(len(tasks)):
            currTask = tasks[i]
            currTask.append(i)
            #PQ1 enqueue time, processingtime, index
            heapq.heappush(pq1, currTask)
        
        firstTask = heapq.heappop(pq1)
        #PQ2 processingtime, index, enqueue time
        heapq.heappush(pq2, [firstTask[1], firstTask[2], firstTask[0]])
        currTime = firstTask[0]

        while pq1:
            print(pq2)
            #process one task in pq2
            #check current time, dequeue from pq1 and add it to pq2 until time is larger
            currTask = heapq.heappop(pq2)
            ans.append(currTask[1])
            currTime = currTime + currTask[0]
            while pq1 and pq1[0][0] <= currTime:
                temp = heapq.heappop(pq1)
                heapq.heappush(pq2, [temp[1], temp[2], temp[0]])
            if len(pq2) == 0 and len(pq1) != 0:
                temp = heapq.heappop(pq1)
                heapq.heappush(pq2, [temp[1], temp[2], temp[0]])
                currTime = temp[0]
        
        #then process whatevers left in pq2
        while pq2:
            currTask = heapq.heappop(pq2)
            ans.append(currTask[1])
            currTime = currTime + currTask[0]

        return ans



        

        