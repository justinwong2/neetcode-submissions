class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        target = n * 2
        temp = []
        ans = []

        def dfs(currWord):
            if len(currWord) == target:
                temp.append(currWord)
                return
            
            dfs(currWord + "(")
            dfs(currWord + ")")

        def validate(word):
            stack = []
            for i in range(0, len(word)):
                curr = word[i]
                if len(stack) > 0 and stack[-1] == "(" and curr == ")":
                    stack.pop()
                else:
                    stack.append(curr)
            if len(stack) == 0:
                return True
            return False

        dfs("")

        for word in temp:
            if validate(word):
                ans.append(word)
        
        return ans
        