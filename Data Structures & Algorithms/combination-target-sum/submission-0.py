class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(index, currSum, currArr):
            if currSum > target:
                return
            if currSum == target:
                ans.append(currArr)
                return
            
            for i in range(index, len(nums)):
                copyArr = currArr.copy()
                copyArr.append(nums[i])
                newSum = currSum + nums[i]
                dfs(i, newSum, copyArr)
            
        dfs(0, 0, [])
        
        return ans