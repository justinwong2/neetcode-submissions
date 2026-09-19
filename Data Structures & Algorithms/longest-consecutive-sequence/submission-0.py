class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest, currLen = 1, 1
        index = 1
        prevVal = nums[0]
        while index < len(nums):
            if nums[index] - 1 == prevVal:
                currLen += 1
                longest = max(longest, currLen)
            elif nums[index] == prevVal:
                index += 1
                continue
            else:
                currLen = 1
            prevVal = nums[index]
            index += 1

        return longest
        