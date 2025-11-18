problem link : https://www.geeksforgeeks.org/problems/articulation-point-1/1

import sys
sys.setrecursionlimit(10**6)

class Solution:
   
    def articulationPoints(self, V, adj):
        self.timer = 0 
        visited = [0] * V 
        tin = [float("inf")] * V # time of insertion
        low = [float("inf")] * V 
        
        res = set()
        for node in range(V):
            if not visited[node]:
                self.dfs(node, -1, visited, adj, tin, low, res)
        return sorted(list(res)) if res else [-1]
    
    def dfs(self, node, parent, visited, adj, tin, low, res):
        visited[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        
        child = 0
        for adjNode in adj[node]:
            if adjNode == parent:
                continue 
            if not visited[adjNode]:
                self.dfs(adjNode, node, visited, adj, tin, low, res)
                low[node] = min(low[node], low[adjNode])
                if low[adjNode] >= tin[node] and parent != -1:
                    res.add(node)
                child += 1
            else:
                low[node] = min(low[node], tin[adjNode])
                
                
        if child > 1 and parent == -1:
            res.add(node)
            

''' Tarjan's Algorithm
    time complexity : O(V + 2E)
    space complexity : O(V + 2E)        
'''
        
