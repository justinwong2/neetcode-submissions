class KthLargest:
    #3rd largest means i only need to keep the top 3 biggest vals in my minHeap, then the smallest value in that heap will be my 3rd largest
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        for i in range(0, len(nums) - k):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) == self.k:
            ans = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, ans)
            return ans
        else:
            heapq.heappop(self.minHeap)
            ans = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, ans)
            return ans
