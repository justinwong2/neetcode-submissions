class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midVal = nums[mid]
            leftVal = nums[left]
            rightVal = nums[right]
            if midVal == target:
                return mid
            elif midVal <= rightVal: #right side confirmed sorted, not sure about left
                if midVal < target and target <= rightVal: 
                    left = mid + 1 #search the right side 
                else:
                    right = mid - 1
            elif leftVal <= midVal: #left side confirm sorted, not sure about right
                if leftVal <= target and target < midVal:
                    right = mid - 1 #search the left side 
                else:
                    left = mid + 1
        
        return -1



