class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #not sorted
        #if i sort is nlogn time complexity
        #i can binary search but i need to lock 2 numbers, end up is n^2(logn) time complexity
        # target == 0
        arr = [] 
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[left] + nums[right]
                if val == target:
                    arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left - 1]:
                        left += 1
                elif val < target:
                    left += 1
                else:
                    right -= 1
        return arr


        