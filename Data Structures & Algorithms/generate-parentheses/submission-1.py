class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        target = n * 2
        ans = []

        def dfs(currWord, currOpen, currClosed):
            if len(currWord) == target and currOpen == currClosed:
                ans.append("".join(currWord))
                return
            #if the number of open brackets is less than half thr acceptable
            #cannot put = because if n== 3 and total chars is 6, adding one more would make openbrackets = 4 which is wrong already
            if currOpen < n:
                currWord.append('(')
                currOpen += 1
                dfs(currWord, currOpen, currClosed)
                currWord.pop()
                currOpen -= 1
            #i only add closed brackets after adding open brackets, which means the closed should always be less than open if i want to add
            if currClosed < currOpen:
                currWord.append(")")
                currClosed += 1
                dfs(currWord, currOpen, currClosed)
                currWord.pop()
                currClosed -= 1

        dfs([], 0,0)
            

        return ans
        