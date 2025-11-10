problem link : https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph

class Solution:
    def isCyclic(self, V, edges):
        visited = [0] * V 
        path = [0] * V 
        graph = [[] for _ in range(V)]
        
        for u, v in edges:
            graph[u].append(v)
        
        for node in range(V):
            if not visited[node]:
                if self.dfs(visited, graph, node, path):
                    return True 
        return False 


    def dfs(self, visited, adj, node, path):
        visited[node] = 1
        path[node] = 1 
        
        for adjNode in adj[node]:
            if not visited[adjNode]:
                if self.dfs(visited, adj, adjNode, path):
                    return True 
            elif path[adjNode]:
                return True 
        
        path[node] = 0 
        return False 

''' DFS
    time complexity : O(V + E)
    space complexity : O(2V)
'''
