class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #find location of all the chests
        #from the position of each chest, do a bfs and then fill the grid lol
        from collections import deque
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
        counter = 1
        while q:
            #take each node, for the neighbours left right up down, if it is -1, pass, if it is not INF, pass becasue i have seen it already or it is a treasure chest
            #get the length of the current so i know when one round of BFS completes
            currSize = len(q)
            print(counter)
            for i in range(currSize):
                currNode = q.popleft()
                currX, currY = currNode[0], currNode[1]
                if currX + 1 < len(grid) and grid[currX + 1][currY] == 2147483647:
                    grid[currX + 1][currY] = counter
                    q.append((currX + 1, currY))
                if currX - 1 >= 0 and grid[currX - 1][currY] == 2147483647:
                    grid[currX - 1][currY] = counter
                    q.append((currX - 1, currY))
                if currY + 1 < len(grid[0]) and grid[currX][currY + 1] == 2147483647:
                    grid[currX][currY + 1] = counter
                    q.append((currX, currY + 1))
                if currY - 1 >= 0 and grid[currX][currY - 1] == 2147483647:
                    grid[currX][currY - 1] = counter
                    q.append((currX, currY - 1))
            counter += 1
    