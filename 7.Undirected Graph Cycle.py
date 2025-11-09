Problem Link : https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    def isCycle(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [0] * V
        for node in range(V):
            if visited[node] == 0:
                if self.dfs(node, visited, graph, -1):
                    return True
        return False

    def dfs(self, node, visited, graph, parent):
        if visited[node] == 0:
            visited[node] = 1
            for adjNode in graph[node]:
                if visited[adjNode] == 1:
                    if adjNode != parent:
                        return True
                else:
                    if self.dfs(adjNode, visited, graph, node):
                        return True
        return False 
        
        
''' DFS 
    time complexity : O(V + 2E)
    space complexity : O(V)
'''


#####################################################################################################################################################


from collections import deque
class Solution:
    def isCycle(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [0] * V
        for node in range(V):
            if visited[node] == 0:
                if self.bfs(node, visited, graph):
                    return True
        return False

    def bfs(self, start, visited, graph):
        q = deque()
        q.append((start, -1))
        visited[start] = 1
        while q:
            node, parent = q.popleft()
            for adjNode in graph[node]:
                if not visited[adjNode]:
                    visited[adjNode] = 1
                    q.append((adjNode, node))
                elif adjNode != parent:
                    return True
        return False
        
''' BFS 
    time complexity : O(V + 2E)
    space complexity : O(V)
'''
