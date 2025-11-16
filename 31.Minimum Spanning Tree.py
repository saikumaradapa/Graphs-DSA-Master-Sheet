Problem Link : https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimum-spanning-tree

Minimum Spanning Tree

###################################################################################################################################################################
# Prim's Algorithms with Priority Queue

from heapq import heapify, heappush, heappop
class Solution:
    def spanningTree(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        visited = [0] * V
        heap = ([(0, 0, -1)]) # cost, node, parent 
        heapify(heap)
        mst = []
        sum = 0
        
        while heap:
            cost, node, parent = heappop(heap)
            if visited[node] == 0:
                visited[node] = 1
                sum += cost
                if parent != -1:
                    mst.append((parent, node))
                
                for curr in graph[node]:
                    heappush(heap, (curr[1], curr[0], node))
        # print(mst)
        return sum
        
''' time complexity : O(E * logE)
    space complexity : O(E)
'''
            
###################################################################################################################################################################
# Kruskal Algorithm with Disjoint Sets 


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n 
    
    def findParent(self, node):
        if self.parent[node] == node:
            return node 
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        
        if ulp_u == ulp_v:
            return False 
        
        if self.size[ulp_u] <= self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v 
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u 
            self.size[ulp_u] += self.size[ulp_v]
            
        self.count -= 1
        return True 
class Solution:
    
    def spanningTree(self, V, adj):
        edges = []
        for u in range(V):
            for v, wt in adj[u]:
                edges.append((u, v, wt))
        
        edges.sort(key = lambda x:x[2])
        DS = DisjointSet(V)
        res = 0 
        
        for u, v, wt in edges:
            res += DS.unionBySize(u, v) * wt
        return res 

''' time complexity : O(E * logE) + O(E * 4 * alpha)
    space complexity : O(E)
'''
