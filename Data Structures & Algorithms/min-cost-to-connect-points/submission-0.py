class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        #to solve this i should find the cost between every point first right
        #then i need to find the min spanning tree to this?

        def calc_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        pq = []
        cost = 0
        currNodes = {}
        # i start with a point, and then i all the possible edges connected to this point into the pq
        # the pq should hold (edge weight, end_node)
        # for each time i deque, i check if the end_node is in currNodes, if it is move on
        # if not, add it to currNodes, add to currCost
        # when currNodes == len(points), break early

        firstPoint = points[0]
        currNodes[(firstPoint[0], firstPoint[1])] = 1
        for i in range(1, len(points)):
            currDistance = calc_distance(firstPoint, points[i])
            heapq.heappush(pq, [currDistance, points[i]])
        print(pq)
        
        while pq:
            if len(currNodes) == len(points):
                break
            curr = heapq.heappop(pq)
            if (curr[1][0], curr[1][1]) in currNodes:
                continue
            else:
                currNodes[(curr[1][0], curr[1][1])] = 1
                cost += curr[0]
                for i in range(len(points)):
                    currPoint = points[i]
                    if (currPoint[0], currPoint[1]) in currNodes or currPoint == curr[1]:
                        continue
                    else:
                        currDistance = calc_distance(curr[1], currPoint)
                        heapq.heappush(pq, [currDistance, currPoint])
        
        return cost


        
        