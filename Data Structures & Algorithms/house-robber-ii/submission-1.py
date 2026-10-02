class Solution:
    def rob(self, nums: List[int]) -> int:
        #at every step, i can choose to rob or not rob
        #since it is a circle, i just need to remember whether i robbed the first house or not
        memo = {}

        def explore(index, currSum, robbedFirst):
            if index >= len(nums):
                return currSum
            #if i go rob first means i cannot rob the last
            if index == len(nums) - 1 and robbedFirst:
                return currSum

            currVal = nums[index]
            if (index, currSum, robbedFirst) in memo:
                return memo[(index, currSum, robbedFirst)]
            
            #keep track of the max
            #dont rob
            temp1 = explore(index+1, currSum, robbedFirst)
            #rob
            if index == 0:
                temp2 = explore(index+2, currSum + currVal, True)
            else:
                temp2 = explore(index+2, currSum + currVal, robbedFirst)
            memo[(index, currSum, robbedFirst)] = max(temp1, temp2)
            return max(temp1, temp2)
        
        return explore(0,0, False)

                


        