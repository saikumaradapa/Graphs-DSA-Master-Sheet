problem link1 : https://www.geeksforgeeks.org/problems/prerequisite-tasks/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=prerequisite-tasks
problem link2 : https://www.geeksforgeeks.org/problems/course-schedule/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=course-schedule

class Solution:
    def findOrder(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        visited = [-1] * n
        
        for u, v in prerequisites:
            graph[u].append(v)
        
        res = []
        for node in range(n):
            if visited[node] == -1:
                if self.dfs(node, graph, visited, res):
                    return []
        return res
        
    def dfs(self, node, graph, visited, res):
        visited[node] = 2
        for adjNode in graph[node]:
            if visited[adjNode] == -1:
                if self.dfs(adjNode, graph, visited, res):
                    return True
            elif visited[adjNode] == 2:
                return True
                
        visited[node] = 1
        res.append(node)
        return False
        
''' DFS
    time complexity : O(V + E)
    space complexity : O(V) 
'''        

########################################################################################################################################################

from collections import deque
class Solution:
    def findOrder(self, n, m, prerequisites):
        adj = [[] for _ in range(n)]
        for v, u in prerequisites:
            adj[u].append(v)
        
        N = V = n
        
        indegree = [0] * V 
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        
        q = deque([])
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            
            for adjNode in adj[node]:
                indegree[adjNode] -= 1 
                if not indegree[adjNode]:
                    q.append(adjNode)
        
        if len(res) == N:
            return res
        return [] 

''' BFS | toposort 
    time complexity : O(V + 2E)
    space complexity : O(V) 
'''      
