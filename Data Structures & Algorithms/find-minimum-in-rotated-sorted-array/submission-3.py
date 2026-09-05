class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        currMin = None

        while left <= right:
            middle = left + (right - left) // 2
            leftVal = nums[left]
            rightVal = nums[right]
            midVal = nums[middle]
            if leftVal <= midVal and midVal <= rightVal: #left side is ascending, right side also ascending, normal array
                return leftVal
            elif midVal > rightVal: #if the middleValue is larger than the rightValue, everything after the rightValue (left side) will be larger than the rightValue, so i need to search the right side
                left = middle + 1
            elif midVal < leftVal: #if the middleValue is smaller than the leftValue, everything after the middle will be larger than middle, therefore i need to search the left side
                right = middle
