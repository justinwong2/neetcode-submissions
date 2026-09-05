class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1, dic2 = {}, {}
        shortestStub = ''
        totalCount = 0
        if len(t) > len(s):
            return ''
        for char in t:
            dic2[char] = dic2.get(char, 0) + 1
        
        left, right = 0, 0

        while right < len(s):
            currChar = s[right]
            #what if i only add to dic1 if it is one of the chars in dic2?
            if currChar in dic2:
                dic1[currChar] = dic1.get(currChar, 0) + 1
                totalCount += 1
                #check the indiv values, if the values dont fufill, shift right and continue
                #if the values DO fufill, log, keep shifting left until no longer fufilled
                for key,value in dic2.items():
                    if key not in dic1 or dic1[key] < value:
                        right += 1
                        break
                else:
                    #if it doesnt break means it fufills, do the left shifting
                    while left <= right:
                        if shortestStub == '' or len(shortestStub) > right-left+1:
                            shortestStub = s[left:right+1]
                        leftChar = s[left]
                        left += 1
                        if leftChar in dic1:
                            totalCount -= 1
                            dic1[leftChar] = dic1[leftChar] - 1
                            if dic1[leftChar] < dic2[leftChar]:
                                break
                    right += 1
            else:
                right += 1
        return shortestStub
