class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        pq = []
        neighbourList = {}
        visited = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        #the distance array keeps track of the minimum effort to get to this step from 0,0
        distance = [[100000000 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                currVal = heights[row][col]
                temp = []
                if row-1 >= 0: #up
                    neigh1 = heights[row-1][col]
                    weight = abs(currVal - neigh1)
                    temp.append((weight, row-1, col))
                if row+1 < len(heights): #down
                    neigh2 = heights[row+1][col]
                    weight = abs(currVal - neigh2)
                    temp.append((weight, row+1, col))
                if col-1 >= 0: #left
                    neigh3 = heights[row][col - 1]
                    weight = abs(currVal - neigh3)
                    temp.append((weight, row, col-1))
                if col+1 < len(heights[0]): #right
                    neigh4 = heights[row][col + 1]
                    weight = abs(currVal - neigh4)
                    temp.append((weight, row, col+1))
                neighbourList[(row, col)] = temp

        print(neighbourList)
        #weight row col
        heapq.heappush(pq, (heights[0][0], 0, 0))
        distance[0][0] = 0
        while pq:
            curr = heapq.heappop(pq)
            weight, row, col = curr[0], curr[1], curr[2]
            if visited[row][col] == 1:
                continue
            else:
                visited[row][col] = 1
                for neighbour in neighbourList[(row, col)]:
                    nw, nr, nc = neighbour[0], neighbour[1], neighbour[2]
                    possible = max(distance[row][col], nw)
                    if possible < distance[nr][nc]:
                        distance[nr][nc] = possible
                        heapq.heappush(pq, (possible, nr, nc))
        return distance[-1][-1]



         