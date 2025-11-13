problem link : https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-weighted-undirected-graph


from heapq import heapify, heappush, heappop
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        graph = [[] for _ in range(n+1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float("inf")] * (n+1)
        dist[1] = 0
        parent = [-1] * (n+1)
        
        heap = [(0, 1)] # (dist, node)
        heapify(heap)
        
        while heap:
            d, node = heappop(heap)
            for curr in graph[node]:
                currDist = d + curr[1]
                
                if currDist < dist[curr[0]]:
                    parent[curr[0]] = node
                    dist[curr[0]] = currDist
                    heappush(heap, (currDist, curr[0]))
                    
        if dist[n] == float("inf"):
            return [-1]
        
        res = [dist[n], n]
        idx = n
        while parent[idx] != -1:
            res.append(parent[idx])
            idx = parent[idx]

        return res
        
''' time complexity : O(E log V)
    space complexity : O(V)
'''   
