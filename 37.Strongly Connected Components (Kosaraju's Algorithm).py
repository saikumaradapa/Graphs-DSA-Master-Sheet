Problem link : https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

class Solution:
    def kosaraju(self, adj):
        n = len(adj)
        stack = []
        visited = [0] * n 
        
        for node in range(n):
            if not visited[node]:
                self.dfs(node, visited, adj, stack, True)
        
        adjT = [[] for _ in range(n)]
        for node in range(n):
            for adjNode in adj[node]:
                adjT[adjNode].append(node)
        
        ssc_count = 0 
        visited = [0] * n
        while stack:
            node = stack.pop()
            if not visited[node]:
                ssc_count += 1
                self.dfs(node, visited, adjT, stack, False)
        return ssc_count 
                
    def dfs(self, node, visited, adjList, stack, flag):
        visited[node] = 1
        for adjNode in adjList[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, adjList, stack, flag)
        if flag:
            stack.append(node)
            
''' 
    time complexity : O(V + E)
    space complexity : O(V + E)
'''
