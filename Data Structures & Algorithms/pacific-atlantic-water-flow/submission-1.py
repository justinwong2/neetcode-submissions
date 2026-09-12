class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #cells adjacent to ocean can flow into it 
        #must be able to flow into both pacific and alatntic
        #basically i want to find cells that can reach both borders of the grid right
        from collections import deque
        pacific  = deque()
        alantic = deque()
        pacificVisited = []
        alanticVisited = []

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0:
                    pacific.append((row, col))
                if row == len(heights) - 1:
                    alantic.append((row, col))
                if col == 0:
                    pacific.append((row, col))
                if col == len(heights[0]) - 1:
                    alantic.append((row, col))
        print(pacific)
        print(alantic)
        
        #so if i do dfs / bfs from the border pacific and the border alantic, then i know which cells they can reach, then i just need to keep the nodes that exist in both
        #the 2 arrays should be the same size because its a rectangle 

        def dfs(node, visited):
            x = node[0]
            y = node[1]
            currHeight = heights[x][y]
            if x-1 >= 0 and heights[x-1][y] >= currHeight and (x-1,y) not in visited:
                visited.append((x-1,y))
                dfs((x-1,y), visited)
            if x+1 < len(heights) and heights[x+1][y] >= currHeight and (x+1,y) not in visited:
                visited.append((x+1,y))
                dfs((x+1,y), visited)
            if y-1 >= 0 and heights[x][y-1] >= currHeight and (x,y-1) not in visited:
                visited.append((x,y-1))
                dfs((x,y-1), visited)
            if y+1 < len(heights[0]) and heights[x][y+1] >= currHeight and (x,y+1) not in visited:
                visited.append((x,y+1))
                dfs((x,y+1), visited)

        for i in range(len(pacific)):
            currPacific = pacific.popleft()
            currAlantic = alantic.popleft()
            if currPacific not in pacificVisited:
                pacificVisited.append(currPacific)
                dfs(currPacific, pacificVisited)
            if currAlantic not in alanticVisited:
                alanticVisited.append(currAlantic)
                dfs(currAlantic, alanticVisited)

        return list(set(pacificVisited) & set(alanticVisited))