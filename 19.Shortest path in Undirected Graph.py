problem link : https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph-having-unit-distance

from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        q = deque([src])
        dist = [float('inf') for _ in range(len(adj))]
        dist[src] = 0
        
        while q:
            node = q.popleft()
            for curr in adj[node]:
                if dist[curr] > dist[node] + 1:
                    dist[curr] = dist[node] + 1
                    q.append(curr)
        
        res = [-1 if num == float('inf') else num for num in dist]
        return res 


''' BFS
    time complexity : O(V + E)
    space complexity : O(V)
'''
