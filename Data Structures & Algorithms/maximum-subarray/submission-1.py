class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        answer = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            currVal = nums[i]
            #at this point, should i add this value to the currMax, or should i just start from this value?
            if currMax + currVal < currVal:
                currMax = currVal
                answer = max(answer, currMax)
            else:
                currMax = currMax + currVal
                answer = max(answer, currMax)
        return answer
        