Problem link : https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1

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
    def maxRemove(self, adj, n):
        maxRow = max(adj, key=lambda x:x[0])[0]
        maxCol = max(adj, key=lambda x:x[1])[1]
        
        ds = DisjointSet(maxRow+maxCol+2)
        stoneNodes = set()
        
        for row, col in adj:
            rowNode = row
            colNode = col + maxRow + 1
            
            ds.unionBySize(rowNode, colNode)
            stoneNodes.add(rowNode)
            stoneNodes.add(colNode)
        
        cnt = 0 
        for stone in stoneNodes:
            if ds.findParent(stone) == stone:
                cnt += 1
        
        # stones - component count 
        return n - cnt


''' 
    time complexity : n * m * 4 alpha
    space complexity : n + m
'''
        
