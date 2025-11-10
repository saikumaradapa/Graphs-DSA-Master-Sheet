problem link : https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort

class Solution:
    def topoSort(self, V, edges):
        visited = [0] * V
        graph = [[] for _ in range(V)]
        stack = []
        
        for u, v in edges:
            graph[u].append(v)
        
        for node in range(V):
            if not visited[node]:
                self.dfs(node, graph, visited, stack)
        return stack[::-1]
    
    def dfs(self, node, graph, visited, stack):
        visited[node] = 1
        for adjNode in graph[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, graph, visited, stack)
        stack.append(node)

''' DFS
    time complexity : O(V + E)
    space complexity : O(V) 
'''        



#########################################################################################################################################################
# Kahn's Algorithm with indegree

from collections import deque
class Solution:
    def topoSort(self, V, edges):
        graph = [[] for _ in range(V)]
        indegree = [0] * V
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        
        topo_sort = []
        while q:
            node = q.popleft()
            topo_sort.append(node)
            for adjNode in graph[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
        
        return topo_sort
        
''' BFS
    time complexity : O(V + E)
    space complexity : O(V) 
'''   
