class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(index, prevArr):
            if index >= len(nums):
                return
            currVal = nums[index]

            newArr1 = prevArr.copy()
            #choose to add
            newArr1.append(currVal)
            newArr2 = prevArr.copy()
            
            if index == len(nums) - 1:
                ans.append(newArr1)
                ans.append(newArr2)
            dfs(index+1, newArr1)
            dfs(index+1, newArr2)
        
        dfs(0, [])
        return ans


