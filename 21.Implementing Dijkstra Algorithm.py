problem link : https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-dijkstra-set-1-adjacency-matrix

from heapq import heapify, heappop, heappush
class Solution:
    def dijkstra(self, V, edges, src):
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        res = [float("inf")] * V
        res[src] = 0
        
        heap = [(0, src)] # (dist, node)
        heapify(heap)
        
        while heap:
            dist, node = heappop(heap)
            for curr in graph[node]:
                currDist = dist + curr[1]
                
                if currDist < res[curr[0]]:
                    res[curr[0]] = currDist
                    heappush(heap, (currDist, curr[0]))
        return res
        
''' time complexity : O(E log V)
    space complexity : O(V)
'''        
