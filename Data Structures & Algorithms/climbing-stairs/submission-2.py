class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        memo ={}
        # at every point i have 2 options, to take 1 step or 2 step
        # i should memo the number of unique ways at my current step height
        # number of ways at n = number of ways at n+1 + number of ways at n+2

        def explore(height):
            if height > n:
                return 0
            if height == n:
                memo[height] = 1
                return 1
            if height in memo:
                return memo[height]
            else:
                temp = explore(height+1) + explore(height+2)
                memo[height] = temp
                return temp

        explore(0)


        return memo[0]