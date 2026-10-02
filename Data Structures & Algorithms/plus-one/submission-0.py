class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        bool1 = False
        for i in range(len(digits) -1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    bool1 = True
        
        if bool1:
            digits.insert(0, 1)
        return digits
        