class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #run a pass to count the number of fresh fruits in total (some might not be reached)
        #find the positions of the rotting fruits also
        #add the rotting fruits to a queue, BFS
        #do until q is empty. if fresh fruit count = 0, retyrb the loop count, else return -1

        from collections import deque
        q = deque()
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        totalFresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    totalFresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        if len(q) == 0 and totalFresh == 0:
            return 0
        elif len(q) == 0 and totalFresh > 0:
            return -1
            
        loop = -1
        while q:
            currLen = len(q)
            loop += 1
            print(grid)
            for i in range(currLen):
                currPos = q.popleft()
                currX, currY = currPos[0], currPos[1]
                if currX + 1 < len(grid) and grid[currX + 1][currY] == 1:
                    q.append((currX + 1, currY))
                    grid[currX + 1][currY] = 2
                    totalFresh -= 1
                if currX - 1 >= 0 and grid[currX - 1][currY] == 1:
                    q.append((currX - 1, currY))
                    grid[currX - 1][currY] = 2
                    totalFresh -= 1            
                if currY + 1 < len(grid[0]) and grid[currX][currY + 1] == 1:
                    q.append((currX, currY + 1))
                    grid[currX][currY + 1] = 2
                    totalFresh -= 1              
                if currY - 1 >= 0 and grid[currX][currY - 1] == 1:
                    q.append((currX, currY - 1))
                    grid[currX][currY - 1] = 2
                    totalFresh -= 1

        if totalFresh > 0:
            return -1
        return loop              
               
