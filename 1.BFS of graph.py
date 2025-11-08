problem link : https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bfs_of_graph

from collections import deque
class Solution:
    def bfs(self, adj):
        res = []
        visited = [0] * len(adj)
        q = deque([0])
        
        visited[0] = 1
        while q:
            node = q.popleft()
            res.append(node)
            
            for adjNode in adj[node]:
                if not visited[adjNode]:
                    q.append(adjNode)
                    visited[adjNode] = 1
        return res


''' space complexity : O(V)        
    time complexity : O(V) + O(2E) - where 2E is the total degree of the graph.
'''
