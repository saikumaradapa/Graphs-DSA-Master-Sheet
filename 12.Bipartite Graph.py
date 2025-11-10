problem link : https://www.geeksforgeeks.org/problems/bipartite-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bipartite-graph

from collections import deque
class Solution:
    def isBipartite(self, V, edges):
        visited = [-1] * V 
        graph = [[] for _ in range(V)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(V):
            if visited[i] == -1 :
                if self.bfs(i, 0, graph, visited) == 0:
                    return 0 
        return 1 
    
    def bfs(self, node, color, graph, visited):
        q = deque([(node, color)])
        
        while q:
            node, color = q.popleft()
            visited[node] = color 
            
            for adjNode in graph[node]:
                if visited[adjNode] == -1:
                    q.append((adjNode, 1-color))
                elif visited[adjNode] == color:
                    return 0 
        return 1

''' time complexity : O(V + 2E)
    space complexity : O(V)
'''  

