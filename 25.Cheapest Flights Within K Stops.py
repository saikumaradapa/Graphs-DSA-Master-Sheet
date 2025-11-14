problem link : https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=cheapest-flights-within-k-stops


from typing import List
from collections import deque
class Solution:

    def CheapestFLight(self, n, flights, src, dst, k):
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        cost = [float("inf")] * n 
        cost[src] = 0
        
        q = deque([(0, src, 0)]) # stops, node, cost
        while q:
            stops, node, price = q.popleft()
            if stops > k:
                continue
            
            for curr in graph[node]:
                adjNode = curr[0]
                adjWt = curr[1]
                if cost + adjWt < cost[adjNode] and stops <= k:
                    cost[adjNode] = cost + adjWt
                    q.append((stops + 1, adjNode, cost + adjWt))
                    
        return cost[dst] if cost[dst] != float("inf") else -1
        
''' can be solved with priority queue (heap) with dijkstra algorithm which cost extra log time
    time complexity : O(E) - at worst all edges will be consider once
    space complexity : O(E)
'''
