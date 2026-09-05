class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left and right start from 0, add the right value into a dict
        #longestCount = 1
        #shift right, check if currValue is repeated
        #if not repeated, increase count
        #if repeated, shift left until no longer repeated.
        #continue until right reaches the end 

        left, right = 0, 0
        dic = {}
        longest = 0
        while right < len(s):
            currLetter = s[right]
            if currLetter not in dic:
                dic[currLetter] = 1
                longest = max(longest, len(dic))
                right += 1
            else:
                dic[currLetter] = dic[currLetter] + 1
                while left < right and dic[currLetter] > 1:
                    currLeft = s[left]
                    dic[currLeft] = dic[currLeft] - 1
                    if dic[currLeft] == 0:
                        dic.pop(currLeft)
                    left += 1
                right += 1
        return longest
