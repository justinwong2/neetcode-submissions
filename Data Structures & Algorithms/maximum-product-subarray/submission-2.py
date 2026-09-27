class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #at each point, i check my current value, if i multiply the next value and it is lesser than the original value, i should just stick to the original value and restart from there
        #is this kind of a greedy problem??
        
        if len(nums) == 1:
            return nums[0]
        currMax = 1 * nums[0]
        maxi = 1 * nums[0]
        currMin = 1 * nums[0]

        for i in range(1, len(nums)):
            currVal = nums[i]
            temp1 = currMax * currVal
            temp2 = currMin * currVal
            currMax = max(temp1, temp2, currVal)
            currMin = min(temp1, temp2, currVal)
            maxi = max(maxi, currMax)

        return maxi 

