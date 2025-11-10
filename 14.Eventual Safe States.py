problem link : https://www.geeksforgeeks.org/problems/eventual-safe-states/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=eventual-safe-states

class Solution:
    def safeNodes(self, V, edges):
        graph = [[] for _ in range(V)]
        visited = [0] * V
        pathVisit = [0] * V
        
        for u, v in edges:
            graph[u].append(v)
        
        for node in range(V):
            if not visited[node]:
                self.dfs(node, graph, visited, pathVisit)
        
        res = [node for node in range(V) if pathVisit[node] == 0]
        return res
    
    def dfs(self, node, graph, visited, pathVisit):
        visited[node] = 1
        pathVisit[node] = 1
        
        for adjNode in graph[node]:
            if not visited[adjNode]:
                if self.dfs(adjNode, graph, visited, pathVisit):
                    return True
            elif pathVisit[adjNode]:
                return True
        
        pathVisit[node] = 0
        return False 

''' time complexity : O(V + E)
    space complexity : O(V)
'''


#####################################################################################################################################################

--> It can also solved with help of Kahn's Algorithm 

1. reverse edges 
2. apply kahn's algo 
3. you will get the result . 

