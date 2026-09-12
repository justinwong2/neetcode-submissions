class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #i have an edge list, for an undirected graph
        #need total number of connected components
        #create a visited array and an adjList
        #for each value in adjList, if it has not been visited, visit it, increase count by 1
        #do either dfs / bfs
        #return count 

        adj = {}
        visited = {}
        count = 0

        def bfs(val):
            visited[val] = 1
            neighbours = adj.get(val, []) #list
            for n in neighbours:
                if visited[n] == 0:
                    bfs(n)

        for edge in edges:
            left, right = edge[0], edge[1]
            temp1 = adj.get(left, [])
            temp1.append(right)
            adj[left] = temp1
            temp2 = adj.get(right, [])
            temp2.append(left)
            adj[right] = temp2
        
        for i in range(n):
            visited[i] = 0
        
        for val in visited:
            if visited[val] == 1:
                continue
            else:
                count += 1
                bfs(val)
        
        return count

        