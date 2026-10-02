class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            leftChar = s[left]
            rightChar = s[right]
            s[left] = rightChar
            s[right] = leftChar
            left += 1
            right -= 1
        
        