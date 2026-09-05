class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCount = 0
        arr = [0] * len(nums)
        for i in nums:
            total = total * i
            if i == 0:
                zeroCount += 1
        if zeroCount > 1:
            return arr
        elif zeroCount == 1:
            mark = 0
            total = 1
            for j in range(len(nums)):
                if nums[j] == 0:
                    mark = j
                else:
                    total = total * nums[j]
            arr[mark] = total
            return arr
        else:
            for i in range(len(nums)):
                arr[i] = int(total / nums[i])
            return arr
        