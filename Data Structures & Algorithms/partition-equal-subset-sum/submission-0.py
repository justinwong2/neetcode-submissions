class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #for each value, i need to decide whether to put it into subset 1 or subset 2
        #need to keep track of the total for each subset 
        #does sorting help??
        answer = False
        memo = {}
        def explore(index, sum1, sum2):
            nonlocal answer
            if index == len(nums):
                if sum1 == sum2:
                    answer = True
                    return True
                return False
            currVal = nums[index]
            if (index, sum1, sum2) not in memo:
                bool1 = explore(index+1, sum1 + currVal, sum2)
                bool2 = explore(index+1, sum1, sum2 + currVal)
                if bool1 or bool2:
                    memo[(index, sum1, sum2)] = True
                    return True
                else:
                    memo[(index, sum1, sum2)] = False
                    return False
            else:
                return memo[(index, sum1, sum2)]
        explore(0,0,0)
        return answer
