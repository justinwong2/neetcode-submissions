class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        dic = {}
        longest = 0

        while right < len(s):
            currLetter = s[right]
            dic[currLetter] = dic.get(currLetter, 0) + 1
            #check whether curr window length - highestFreq <= k
            #if  yes, update, shift window to the right and continue
            #if no, shift window to the left until it fufuils again, then shift right once
            highestCount = max(dic.values())
            if right-left+1-highestCount <= k:
                longest = max(longest, right-left+1)
                right += 1
            else:
                while right-left+1-highestCount > k:
                    leftLetter = s[left]
                    dic[leftLetter] = dic[leftLetter] - 1
                    left += 1
                    highestCount =  max(dic.values())
                right += 1
        
        return longest


        