class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maxHeap then pop it k -1 times, then return the next pop
        import heapq
        heapq.heapify_max(nums)
        for i in range(k-1):
            heapq.heappop_max(nums)
        return heapq.heappop_max(nums)

        