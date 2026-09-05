class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        
        sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(sorted_dict)
        arr = []
        for j in range(k):
            arr.append(sorted_dict[j][0])
        return arr
