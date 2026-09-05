class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d = {}
        for char in s1:
            d[char] = d.get(char, 0) + 1
        
        #initialize dict for the initial window 
        d2 = {}
        left = 0
        right = len(s1) - 1
        for i in range(left, len(s1)):
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        while right < len(s2):
            #check if current window fufills the criteria
            if d2.items() <= d.items():
                return True
            #removoe left, shift and add right
            leftChar = s2[left]
            d2[leftChar] = d2.get(leftChar) - 1
            if d2[leftChar] == 0: 
                d2.pop(leftChar)
            left += 1
            right += 1
            if right == len(s2):
                return False
            rightChar = s2[right]
            d2[rightChar] = d2.get(rightChar, 0) + 1
        return False

