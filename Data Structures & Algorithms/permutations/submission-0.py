class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        taken = [False] * len(nums)

        def dfs(currArr, takenArr):
            if len(currArr) == len(nums):
                ans.append(currArr.copy())
                return
            
            for i in range(0, len(takenArr)):
                if takenArr[i] == False:
                    takenArr[i] = True
                    currArr.append(nums[i])
                    dfs(currArr, takenArr)
                    takenArr[i] = False
                    currArr.pop()
        
        dfs([], taken)
        return ans
