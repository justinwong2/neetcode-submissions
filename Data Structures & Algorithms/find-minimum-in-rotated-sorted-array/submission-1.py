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
            elif midVal > rightVal: #left side ascending, right side not ascending, smallest val must be on the right
                left = middle + 1
            elif midVal < leftVal: #left side not ascending, right side ascending, smallest must be within the left
                right = middle
