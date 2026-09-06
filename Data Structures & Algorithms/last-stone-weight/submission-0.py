class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 2 heaviest stones - maxHeap
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop_max(maxHeap)
            stone2 = heapq.heappop_max(maxHeap)
            if stone1 == stone2:
                continue
            else:
                stone = abs(stone1 - stone2)
                heapq.heappush_max(maxHeap, stone)
        
        if len(maxHeap) == 0:
            return 0
        else:
            return heapq.heappop_max(maxHeap)

        