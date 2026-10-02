class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #so basically at each step, i can check whether to take or not to take
        #if i take, the remaining word gets shorter then i explore
        #if i dont take, my current word gets longer
        #then each time its just a dictionary check
        #basically i can memo at this point, is it possible for me to use up all the words
        memo = {}

        def explore(currIndex, prevClearedIndex):
            print(currIndex, prevClearedIndex)
            if currIndex == len(s):
                if s[prevClearedIndex + 1: currIndex] in wordDict:
                    return True
                else:
                    return False
            
            if (currIndex, prevClearedIndex) in memo:
                return memo[(currIndex, prevClearedIndex)]

            bool1, bool2 = False, False
            #if can take and choose to take
            if s[prevClearedIndex + 1: currIndex + 1] in wordDict:
                bool1 = explore(currIndex + 1, currIndex)
            
            #choose to not take at this point and continue
            bool2 = explore(currIndex+1, prevClearedIndex)

            if bool1 or bool2:
                memo[(currIndex, prevClearedIndex)] = True
                return True
            memo[(currIndex, prevClearedIndex)] = False
            return False

        return explore(0, -1)
            
        