class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for i in range(len(asteroids)):
            curr = asteroids[i]
            if curr >= 0 or len(ans) == 0:
                ans.append(curr)
            else:
                #if its negative, i need to start popping
                #while answer is not empty and the top answer is non negative and my current abs is larger than the top of the stack
                while len(ans) > 0 and ans[-1] >= 0 and abs(curr) > ans[-1]:
                    ans.pop()
                #if equal pop both
                if len(ans) > 0 and ans[-1] >= 0 and abs(curr) == ans[-1]:
                    ans.pop()
                elif len(ans) > 0 and ans[-1] >= 0 and abs(curr) < ans[-1]: #if my curr negative value is smaller, dont add
                    continue
                else:
                    ans.append(curr)
        return ans

        