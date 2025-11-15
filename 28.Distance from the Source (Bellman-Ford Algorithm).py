problem link : https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=distance-from-the-source-bellman-ford-algorithm


class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8] * V
        dist[src] = 0
        
        for i in range(V-1):
            for u, v, w in edges:
                if dist[u] != 10**8 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[u] + w < dist[v]:
                return [-1]
        
        return dist

''' Bellman-Ford
    time complexity : O(V * E)
    space complexity : O(V)
'''

