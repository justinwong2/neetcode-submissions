class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        #shortest path from source notes to all notes
        #BFS??
        visited = [0] * (n + 1)
        timeTaken = 0
        dic = {}
        #key should be the source nodes, val should be (time, target)
        for i in range(len(times)):
            currTime = times[i]
            #(source, target, time)
            arr = dic.get(currTime[0], [])
            arr.append([currTime[2], currTime[1]])
            dic[currTime[0]] = arr
        
        pq = []
        visited[k] = 1
        for i in dic.get(k, []):
            heapq.heappush(pq, [i[0], i[1]])
        print(pq)
        
        while pq:
            curr = heapq.heappop(pq)
            if visited[curr[1]] == 1:
                continue
            else:
                visited[curr[1]] = 1
                for j in dic.get(curr[1], []):
                    heapq.heappush(pq, [curr[0]+ j[0], j[1]])
                timeTaken = max(timeTaken, curr[0])
        
        for i in range(1, n+1):
            if visited[i] == 0:
                return -1
        return timeTaken