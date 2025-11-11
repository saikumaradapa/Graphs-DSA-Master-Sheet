problem link : https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=direct-acyclic-graph


1. find the stack in topo sort 
2. relaxation of edges with distances 

from typing import List
class Solution:
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(V)]
        stack = []
        visited = [0] * V
        
        for u, v, w in edges:
            graph[u].append((v, w))
        
        for node in range(V):
            if not visited[node]:
                self.dfs(node, graph, visited, stack)
        
        dist = [float("inf") for _ in range(V)]
        dist[0] = 0
        while stack:
            node = stack.pop()
            for adjNode, wt in graph[node]:
                dist[adjNode] = min(dist[adjNode], dist[node] + wt)
        return [num if num != float("inf") else -1 for num in dist] 
        
    def dfs(self, node, graph, visited, stack):
        visited[node] = 1
        for adjNode, wt in graph[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, graph, visited, stack)
        stack.append(node)

''' DFS
    time complexity : O(V + E)
    space complexity : O(V)
'''
