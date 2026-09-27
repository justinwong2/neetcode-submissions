class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #or i can try to work backwards and bring amount down to 0??
        #actually no i dont think theres a difference lol
        #for each value between 1-amount, i want to store the least amount of coins to get here??
        memo = [100000000] * (amount + 1)

        def explore(currAmount, numCoins):
            if currAmount > amount:
                return
            if numCoins < memo[currAmount]:
                memo[currAmount] = numCoins
                for value in coins:
                    explore(currAmount +  value, numCoins + 1)
            else:
                return
            
        explore(0, 0)
        if memo[amount] == 100000000:
            return -1
        return memo[amount]
            
        