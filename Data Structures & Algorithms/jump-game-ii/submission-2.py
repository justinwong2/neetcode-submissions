class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1
        currIndex = 0
        numJumps = [None] * len(nums)
        numJumps[len(nums) - 1] = 0
        
        #jumping the furthest each time might not be optimal
        #should i work backwards?
        #for each spot from the back, i calc whats the least number of jumps required to reach the end
        #im like memoising as i go?
        for i in range(len(nums) - 2, -1, -1):
            currVal = nums[i]
            maxEndPos = currVal + i
            minimum = numJumps[i + 1]
            for j in range(i + 1, maxEndPos + 1):
                if j >= len(nums):
                    continue
                currMinimumJumps = numJumps[j]
                minimum = min(currMinimumJumps, minimum)
            numJumps[i] = minimum + 1
        return numJumps[0]

            
        