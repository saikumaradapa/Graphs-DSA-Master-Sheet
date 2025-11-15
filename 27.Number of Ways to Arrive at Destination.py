problem link : https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=%2Fnumber-of-ways-to-arrive-at-destination


from heapq import heapify, heappush, heappop
class Solution:
    def countPaths(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float("inf")] * V
        ways = [0] * V
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)] # dist, node
        heapify(heap)
        
        while heap:
            d, node = heappop(heap)
            for curr in graph[node]:
                adjNode = curr[0]
                adjWt = curr[1]
                
                if d + adjWt < dist[adjNode]:
                    dist[adjNode] = d + adjWt
                    ways[adjNode] = ways[node]
                    heappush(heap, (dist[adjNode], adjNode))
                elif d + adjWt == dist[adjNode]:
                    ways[adjNode] += ways[node]
        
        return ways[-1]
                


''' time complexity : O(E logV)
    space complexity : O(n)
'''
