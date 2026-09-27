class Solution:
    def numDecodings(self, s: str) -> int:
        #need to find the number of ways to decode it 
        #for a value to be valid, cannot start with a leading 0, and has to be in the range of 1-26
        #if s starts with a 0, return 0
        #at each point, decide whether it is alone or pair it with the previous number 
        #if it is alone, the next number can either be alone or paired with it??
        #but if i pair it with the previous number, means the next number HAS to be solo
        memo = {}

        if s[0] == '0':
            return 0

        def explore(index, prevLetter):
            if index == len(s):
                return 1
            currLetter = s[index]
            temp1, temp2 = 0, 0
            if (index, prevLetter) not in memo:
                if len(prevLetter) == 1:
                    if currLetter != '0':
                        temp1 = explore(index+1, currLetter)
                    if int(prevLetter + currLetter) <= 26:
                        temp2 = explore(index+1, prevLetter + currLetter)
                elif len(prevLetter) == 2:
                    if currLetter != '0':
                        temp1 = explore(index+1, currLetter)
                memo[(index, prevLetter)] = temp1 + temp2
                return temp1 + temp2
            else:
                return memo[(index, prevLetter)]
        
        return explore(1, s[0])
        



        
