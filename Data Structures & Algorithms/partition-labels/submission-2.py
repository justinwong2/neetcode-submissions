class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            char = s[i]
            arr = dic.get(char, [])
            arr.append(i)
            dic[char] = arr

        currIndex = 0
        #answer stores the length of each substring
        ans = []
        while currIndex < len(s):
            currLetter = s[currIndex]
            endIndex = dic.get(currLetter)[-1]
            if currIndex == endIndex:
                ans.append(1)
                currIndex += 1
                continue
            lastj = currIndex
            while True:
                org = endIndex
                for j in range(lastj, endIndex):
                    lastj = j
                    tempEnd = dic.get(s[j])[-1]
                    if tempEnd > endIndex:
                        endIndex = tempEnd
                        break
                if org == endIndex:
                    break
            ans.append(endIndex - currIndex + 1)
            currIndex = endIndex + 1
        return ans