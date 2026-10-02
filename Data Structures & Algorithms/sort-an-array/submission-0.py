class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            n = len(arr)
            if n == 1:
                return arr
            temp1 = merge_sort(arr[0:n//2])
            temp2 = merge_sort(arr[n//2: n])


            ans = []
            i, j = 0, 0
            while i < len(temp1) or j < len(temp2):
                if i == len(temp1):
                    ans.append(temp2[j])
                    j += 1
                    continue
                elif j == len(temp2):
                    ans.append(temp1[i])
                    i += 1
                    continue
                else:
                    if temp1[i] < temp2[j]:
                        ans.append(temp1[i])
                        i += 1
                    else:
                        ans.append(temp2[j])
                        j += 1
            return ans
        
        return merge_sort(nums)

        

        