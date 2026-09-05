class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #ideal is to buy low and sell high
        #keep track of the max profit
        #what if i have an array where array[i] gives me the highest price ive seen in the future
        #then i just need loop through prices once, for each day, check what the profit is if i buy today and sell at the max future price, keep track of the highest profit
        #return profit if it is larger than 0, else return 0

        arr = [0] * len(prices)
        tempHighest = 0
        for i in range(0, len(prices)):
            currPrice = prices[-1-i]
            arr[-1-i] = tempHighest
            tempHighest = max(tempHighest, currPrice)

        maxProfit = 0
        for j in range(0, len(prices)):
            profit = arr[j] - prices[j]
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
        