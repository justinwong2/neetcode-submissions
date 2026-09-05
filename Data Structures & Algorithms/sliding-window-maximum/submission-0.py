class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        ans = []
        dic = {}
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        while right < len(nums):
            ans.append(max(dic))
            dic[nums[left]] = dic[nums[left]] - 1
            if dic[nums[left]] == 0:
                dic.pop(nums[left])
            left += 1
            right += 1
            if right < len(nums):
                dic[nums[right]] = dic.get(nums[right], 0) + 1
        return ans


        