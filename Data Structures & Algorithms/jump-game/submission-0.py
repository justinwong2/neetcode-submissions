class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #isnt this sort of a backtracking one?
        #for each position, i explore all the other posiotions that i can reach from here
        #base case if its a 0 then i return early
        #i just need soemthing to return true
        #if i can jump to the last index then i return True
        #technically if i can jump over the last index means i can reach the last index also, dont need to worry about overshotting
        if len(nums) == 1:
            return True
        
        target = len(nums) - 1
        #i should memo, if i have already explored this number, i dont need to run it again?
        memo = {}

        def explore(currIndex):
            currVal = nums[currIndex]
            if currIndex >= target:
                return True
            elif currVal == 0:
                return False
            for i in range(1, currVal + 1):
                if currIndex + i not in memo:
                    memo[currIndex + i] = 1
                    ans = explore(currIndex + i)
                    if ans:
                        return True
        
        ans = explore(0)
        if ans is None:
            return False
        return ans
        