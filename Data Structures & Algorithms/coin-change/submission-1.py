class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #i am storing the least number of coins i need to get to the curr value within memo
        #least amount of coins at this point = least amount of coins at the prev point + 1
        memo = [100000000] * (amount + 1)
        memo[0] = 0

        for index in range(1, len(memo)):
            currMin = 100000000
            for coin in coins:
                if index - coin < 0:
                    pass
                else:
                    currMin = min(currMin, memo[index-coin])
            if currMin == 100000000:
                memo[index] = currMin
            else:
                memo[index] = currMin + 1
        
        if memo[amount] == 100000000:
            return -1
        return memo[amount]
        