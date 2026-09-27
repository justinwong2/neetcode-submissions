class Solution:
    def rob(self, nums: List[int]) -> int:
        #if i rob current, i need to skip one
        #if i dont rob the current, i can rob the next one which may have a higher total
        #isnt this backtracking(??) where is the dp portion?

        memo = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums) - 1, -1, -1):
            #what is the maximum amount of money i can have in this spot when working backwards??
            currAmount = nums[i]
            if i == len(nums) - 1:     
                memo[i] = currAmount
            else:
                if i == len(nums) - 2:
                    memo[i] = max(currAmount, memo[i+1])
                    continue
                currMax = max(memo[i+1], currAmount + memo[i+2])
                memo[i] = currMax
        
        return memo[0]


