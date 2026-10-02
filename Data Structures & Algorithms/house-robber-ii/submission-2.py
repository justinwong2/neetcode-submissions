class Solution:
    def rob(self, nums: List[int]) -> int:
        #at every step, i can choose to rob or not rob
        #since it is a circle, i just need to remember whether i robbed the first house or not
        memo = {}
        #in my memo, i want to keep track of the max amount i have at this index point??

        def explore(index, robbedFirst):
            if index >= len(nums):
                return 0
            #if i go rob first means i cannot rob the last
            if index == len(nums) - 1 and robbedFirst:
                return 0

            currVal = nums[index]
            if (index, robbedFirst) in memo:
                return memo[(index, robbedFirst)]
            
            #keep track of the max
            #dont rob
            temp1 = explore(index+1, robbedFirst)
            #rob
            if index == 0:
                temp2 = explore(index+2, True)
            else:
                temp2 = explore(index+2, robbedFirst)
            memo[(index, robbedFirst)] = max(temp1, temp2 + currVal)
            return max(temp1, temp2 + currVal)
        
        return explore(0, False)

                


        