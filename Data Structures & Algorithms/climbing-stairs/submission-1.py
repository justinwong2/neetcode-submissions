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
                return 1
            if height+1 in memo:
                temp1 = memo[height+1]
            else:
                temp1 = explore(height+1)
                memo[height+1] = temp1
            if height+2 in memo:
                temp2 = memo[height+2]
            else:
                temp2 = explore(height+2)
                memo[height+2] = temp2
            memo[height] = temp1 + temp2
            return temp1+temp2
        explore(0)


        return memo[0]