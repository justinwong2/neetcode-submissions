class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        if m == 0:
            return False
        n = len(matrix[0])
        front = 0
        back = m - 1
        while front < back:
            middle = front + (back - front) // 2
            midVal = matrix[middle][0]
            if midVal == target:
                return True
            elif midVal > target:
                back = middle - 1
            elif midVal < target and target < matrix[middle+1][0]:
                back = middle
                break
            elif midVal < target and target >= matrix[middle+1][0]:
                front = middle + 1
        
        rowSearch = back
        i = 0
        j = n - 1

        while i <= j:
            middle = i + (j - i) // 2
            val = matrix[rowSearch][middle]
            if val == target:
                return True
            elif val < target:
                i = middle + 1
            else:
                j = middle - 1
        return False