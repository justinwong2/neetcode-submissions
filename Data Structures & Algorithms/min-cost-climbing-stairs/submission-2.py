class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #i can start from index 0 or index 1
        #at every step, i can choose to take 1 or 2 steps. I have to pay the cost of the current step
        # if index is the end, return min 
        # i want to try the bottom up approach
        
        #at each step, the min cost of climbing the stairs is the currCost + the min(n+1, n+2)
        if len(cost) == 1:
            return cost[-1]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        
        dp = [100000] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        print(dp)
        return min(dp[0], dp[1])