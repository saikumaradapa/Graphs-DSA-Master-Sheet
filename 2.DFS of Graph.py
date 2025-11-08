problem link : https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph

class Solution:
    def dfs(self, adj):
        visited = [0] * len(adj)
        res = []
        for node in range(len(adj)):
            if visited[node] == 0:
                self.visit(node, visited, adj, res)
        return res
        
    def visit(self, node, visited, adj, res):
        visited[node] = 1
        res.append(node)
        for adjNode in adj[node]:
            if visited[adjNode] == 0:
                self.visit(adjNode, visited, adj, res)

''' time complexity : O(V+ 2E)
    space complexity : O(V)
'''
