class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        endIndex = len(nums1) - 1
        num1End = m - 1
        num2End = n - 1
        while endIndex >= 0 and num2End >= 0 and num1End >= 0:
            currNum1 = nums1[num1End]
            currNum2 = nums2[num2End]
            if currNum1 >= currNum2:
                nums1[endIndex] = currNum1
                nums1[num1End] = 0
                num1End -= 1
                endIndex -= 1
            else:
                nums1[endIndex] = currNum2
                num2End -= 1
                endIndex -= 1
        while endIndex >= 0 and num2End >= 0:
            nums1[endIndex] = nums2[num2End]
            endIndex -= 1
            num2End -= 1



        