problem link : https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=city-with-the-smallest-number-of-neighbors-at-a-threshold-distance


from heapq import heappush, heappop
from typing import List

class Solution:
    def dijkstra(self, S, adj, n):
        dist = [float('inf')] * n 
        dist[S] = 0
        heap = [(0, S)] # (distance, node)
        
        while heap:
            d, node = heappop(heap)
            for neighbor, weight in adj[node]:
                newDist = d + weight
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    heappush(heap, (newDist, neighbor))
        return dist
    
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        distanceMatrix = [self.dijkstra(i, adj, n) for i in range(n)]
        
        minReachableCities = float('inf')
        cityWithMinReachableCities = -1
        
        for i in range(n):
            reachableCities = sum(1 for dist in distanceMatrix[i] if dist <= distanceThreshold)
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                cityWithMinReachableCities = i
        
        return cityWithMinReachableCities

        
''' time complexity : O(n * m logn)
    space complexity : O(n ^ 2)
'''

#######################################################################################################################################################

from typing import List
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        dist = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w 
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    
                    if dist[i][via] == float("inf") or dist[via][j] == float("inf"):
                        continue 
                    if dist[i][via] + dist[via][j] < dist[i][j]:   
                        dist[i][j] = dist[i][via] + dist[via][j]
        
        cityCnt = float("inf")
        cityNo = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= cityCnt:
                cityCnt = cnt
                cityNo = i
        
        return cityNo

''' time complexity : O(n ^ 3)
    space complexity : O(n ^ 2)
'''
