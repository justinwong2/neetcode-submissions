class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = None
        for s in strs:
            if shortest is None:
                shortest = len(s)
            else:
                shortest = min(shortest, len(s))
        count = 0
        for i in range(shortest):
            currChar = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != currChar:
                    return strs[0][:i]
            count += 1
        return strs[0][:count]
        