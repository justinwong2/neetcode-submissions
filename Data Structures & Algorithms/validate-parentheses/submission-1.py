from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }

        q = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                q.append(char)
            else:
                if len(q) == 0:
                    return False
                elif d[char] == q[-1]:
                    q.pop()
                else:
                    return False
        
        return len(q) == 0