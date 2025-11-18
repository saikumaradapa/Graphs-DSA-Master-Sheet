problem link : https://leetcode.com/problems/critical-connections-in-a-network/description/

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [0] * n 
        tin = [float("inf")] * n # time of insertion
        low = [float("inf")] * n
        bridges = []
        self.timer = 1

        for node in range(n):
            if not visited[node]:
                self.dfs(node, -1, visited, adj, tin, low, bridges)
        return bridges
    
    def dfs(self, node, parent, visited, adj, tin, low, bridges):
        visited[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1

        for adjNode in adj[node]:
            if adjNode == parent:
                continue
            if not visited[adjNode]:
                self.dfs(adjNode, node, visited, adj, tin, low, bridges)
                low[node] = min(low[node], low[adjNode])
                # node --- adjNode     check for edge
                if low[adjNode] > tin[node]:
                    bridges.append([node, adjNode])
            else:
                low[node] = min(low[node], low[adjNode])

''' Tarjan's Algorithm
    time complexity : O(V + 2E)
    space complexity : O(V + 2E)        
'''

