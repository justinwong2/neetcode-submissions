class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = {}

        for course in prerequisites:
            pre = course[1]
            post = course[0]
            temp = adjList.get(pre, [])
            temp.append(post)
            adjList[pre] = temp
            visited[pre] = 0
            visited[post] = 0
        
        def dfs(prereq):
            currNeighbours = adjList.get(prereq, []) #list
            visited[prereq] = 1
            for n in currNeighbours:
                #if this neighbour has already been fully explored 
                if visited[n] == 2:
                    continue
                #if this neighbour has yet to been explored
                elif visited[n] == 0:
                    boolean = dfs(n)
                    if boolean == False:
                        return False
                #if someone else is currently visiting it
                elif visited[n] == 1:
                    return False
            visited[prereq] = 2
            return True
        
        for prereq in adjList:
            if visited[prereq] == 0:
                boolean = dfs(prereq)
                if boolean == False:
                    return False
        return True
        

        