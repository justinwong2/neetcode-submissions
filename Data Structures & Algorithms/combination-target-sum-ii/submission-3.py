class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #start from the start
        #at every step, choose to take the current or move on
        #if it exceeds target, return
        #if equal target, add to final array

        ans = []

        def dfs(index, currSum, currArr):
            if currSum == target:
                ans.append(currArr.copy())
                return
            if index >= len(candidates):
                return
            elif currSum > target:
                return
            #choose to take and go next, or just go next
            currVal = candidates[index]
            currArr.append(currVal)
            currSum += currVal
            dfs(index+1, currSum, currArr)
            currArr.pop()
            currSum -= currVal
            #skip, if the previous value is the same,
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, currSum, currArr)  
    
        candidates.sort()
        dfs(0,0,[])

        return ans
            

        