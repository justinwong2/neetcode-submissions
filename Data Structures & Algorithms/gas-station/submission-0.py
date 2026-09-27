class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #so cost is the cost of moving to the next gas station
        #check if the total gas avail is >= cost, if it is not, return -1
        #if there is, it is guaranteed to have 1 answer
        #this is the greedy part at each index, i check if i have enough to move forward
        #if i dont, there is no way i can start from here, check the next
        #else, continue to the nexr station and check
        #if i ever drop below 0, i fail and i need to check start from the next gas station
        #this works becasue everytime i move forward, the amount of gas i have is 0 or more
        #if i start fresh, i will have 0
        #so if i fail starting from a -> c, starting from b would mean i would have <= amount of gas when i moved from a -> b, so no point checking b

        totalGas = 0
        totalCost = 0
        diff = [0] * len(gas)
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            diff[i] = gas[i] - cost[i]
        
        if totalGas < totalCost:
            return -1

        currGas = 0
        currAns = -1
        for i in range(len(gas)):
            currDiff = diff[i]
            if currGas + currDiff >= 0:
                if currAns == -1:
                    currAns = i
                currGas = currGas + currDiff
            else:
                currAns = -1
                currGas = 0
        return currAns

