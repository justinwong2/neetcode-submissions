class MedianFinder:

    def __init__(self):
        import heapq
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        #if both are empty just add to the left which is the max
        if len(self.minHeap) == len(self.maxHeap) == 0:
            heapq.heappush_max(self.maxHeap, num)
        else:
            currVal = heapq.heappop_max(self.maxHeap)
            if num < currVal:
                heapq.heappush_max(self.maxHeap, num)
            else:
                heapq.heappush(self.minHeap, num)
            heapq.heappush_max(self.maxHeap, currVal)
            #if left side is imbalanced by more than 1
            if len(self.maxHeap) + 1< len(self.minHeap):
                #pop the right, add to left
                temp = heapq.heappop(self.minHeap)
                heapq.heappush_max(self.maxHeap, temp)
            #i want my right side to be either balanced or larger
            elif len(self.maxHeap) > len(self.minHeap):
                temp = heapq.heappop_max(self.maxHeap)
                heapq.heappush(self.minHeap, temp)


    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) == 1:
            temp1 = heapq.heappop_max(self.maxHeap)
            heapq.heappush_max(self.maxHeap, temp1)
            return temp1
        if (len(self.maxHeap) + len(self.minHeap)) % 2 != 0:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, temp)
            return temp
        else:
            temp1 = heapq.heappop_max(self.maxHeap)
            heapq.heappush_max(self.maxHeap, temp1)
            temp2 = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, temp2)
            return float((temp1 + temp2) / 2)
        
        