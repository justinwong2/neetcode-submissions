class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #closest points means smallest distance
        #min heap
        import heapq
        minHeap = []

        for point in points:
            x1, y1 = point[0], point[1]
            distance = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
            heapq.heappush(minHeap, (distance, point))
        print(minHeap)
        ans = []
        for i in range(0, k):
            curr = heapq.heappop(minHeap)
            ans.append(curr[1])
        return ans       