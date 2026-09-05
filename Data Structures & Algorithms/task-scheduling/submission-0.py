class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the task that should be performed first is the one that is the most frequent to the least frequent
        # would a PQ work? i store the (letter, count), and then sort by count
        # for each turn, i poll the PQ for the highest count, minus 1 from that count, add to another data structure if the count is not 0, tracking (letter, count, cooldown), then i also reduce the count by 1 for everything else in that data structure, for those that cooldown is 0 i add it back to the PQ.
        #if both the PQ and the cooldown structure is empty then it ends. 
        cycle = 0
        d = {}
        heap = []
        cooldownHeap = []
        for task in tasks:
            d[task] = d.get(task, 0) + 1
        for task, count in d.items():
            heapq.heappush(heap, (-count, task))

        while len(heap) > 0 or len(cooldownHeap) > 0:
            cycle += 1
            if len(heap) > 0:
                count, task = heapq.heappop(heap)
                count += 1
                if count < 0:
                    heapq.heappush(cooldownHeap, (cycle+n, count, task))
            while len(cooldownHeap) > 0:
                cycleCount, count, task = cooldownHeap[0]
                if cycle >= cycleCount:
                    cycleCount, count, task = heapq.heappop(cooldownHeap)
                    heapq.heappush(heap, (count, task))
                else:
                    break
        return cycle 
