problem link : https://www.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number_of_provinces


class Solution:
    
    def dfs(self, node, visited, graph):
        visited[node] = 1
        for adjNode in graph[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, graph)
    
    def numProvinces(self, adj, V):
        graph = [[] for _ in range(V)]
        
        for u in range(V):
            for v in range(V):
                if u != v and adj[u][v] :
                    graph[u].append(v)
                    
        visited = [0] * V
        cnt = 0
        
        for i in range(V):
            if not visited[i]:
                cnt += 1
                self.dfs(i, visited, graph)
        return cnt 

''' time complexity : O(V + 2E)
    space complexity : O(V)
'''

################################################################################################################################################

class Solution:
    def dfs(self, node, visited, adj, V):
        visited[node] = 1
        for neighbor in range(V):
            # neighbor connected AND not yet visited
            if adj[node][neighbor] and not visited[neighbor]:
                self.dfs(neighbor, visited, adj, V)

    def numProvinces(self, adj, V):
        """
        Count connected components directly on the adjacency matrix.

        Time:  O(V^2) — every DFS scans a full row of V entries; across all
                        nodes that's V rows x V columns = V^2.
        Space: O(V)   — visited array + recursion stack (O(V) worst case).

        A province = one connected component. Start a DFS from each unvisited
        node; each fresh DFS marks one whole component, so the number of DFS
        launches is the province count.
        """
        visited = [0] * V
        count = 0

        for i in range(V):
            if not visited[i]:
                count += 1
                self.dfs(i, visited, adj, V)

        return count




################################################################################################################################################
# using DisJoint Sets 


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
    def numProvinces(self, adj, V):
        DS = DisjointSet(V)
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] and i != j:
                    DS.unionBySize(i, j)
        
        return DS.count 
        
''' time complexity : O(V^2 * 4 alpha)
    space complexity : O(V)
'''
