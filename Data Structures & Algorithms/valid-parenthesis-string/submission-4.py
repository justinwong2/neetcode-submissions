class Solution:
    def checkValidString(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        wild = deque()
        
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            elif c == ")":
                if len(stack) == 0:
                    if len(wild) <= 0:
                        return False
                    else:
                        wild.pop()
                else:
                    stack.pop()
            else:
                wild.append(i)
        
        if len(stack) == 0:
            return True
        elif len(wild) < len(stack):
            return False
        #for each value in the stack (, i can only use a wild card that comes after it.
        for i in range(len(stack)):
            curr = stack.pop()
            currWild = wild.pop()
            if curr > currWild:
                return False
            

        return True
        