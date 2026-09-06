class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic ={'2':["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]}
        
        ans = []
        if len(digits) == 0:
            return ans
    
        def backtrack(index, currArr):
            if index == len(digits):
                ans.append("".join(currArr))
                return
            currNumber = digits[index]
            possibleArr = dic[currNumber]
            for c in possibleArr:
                currArr.append(c)
                backtrack(index + 1, currArr)
                currArr.pop()
        backtrack(0, [])
        return ans