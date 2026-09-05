class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 =''
        s1 = s1.join([char for char in s if char.isalnum()])
        left = 0
        right = len(s1) - 1
        while left <= right:
            if s1[left].lower() != s1[right].lower():
                return False
            left += 1
            right -= 1
        return True
        