Problem Link : https://www.geeksforgeeks.org/problems/maximum-connected-group/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=maximum-connected-group


#################################################################################################################################################################################
# my solution with disjointSets || 718 / 1115 test cases 

class DisjointSet:
    def __init__(self, n):
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]
    
    def findPar(self, node):
        if node == self.parent[node]:
            return node 
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        ulp_u = self.findPar(u)
        ulp_v = self.findPar(v)

        if ulp_u == ulp_v:
            return  
        if self.size[ulp_u] >= self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v 
            self.size[ulp_v] += self.size[ulp_u]     


from typing import List


class Solution:
    
    def isValid(self, x, y, n, m):
        return( (0<= x < n) and (0<= y < m))
        
    def MaxConnection(self, grid : List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = DisjointSet(n * m)
        dx = (0, -1, 0, 1)
        dy = (-1, 0, 1, 0)
        ones_present = False 
        

        zeros_list = []


        for u in range(n):
            for v in range(m):
                if grid[u][v] == 1:
                    ones_present = True 
                    for k in range(4):
                        x = u + dx[k]
                        y = v + dy[k] 

                        if self.isValid(x, y, n, m) and grid[x][y]: 
                            currPos = (u * n) + v 
                            adjPos = (x * n) + y 
                            ds.union(currPos, adjPos)
                else:
                    zeros_list.append((u, v))                  
        
        if not zeros_list:
            return n * m
        elif not ones_present:
            return 1

        res = 0
        for u, v in zeros_list:
            adjParents = set()
            for k in range(4):
                x = u + dx[k]
                y = v + dy[k]

                if self.isValid(x, y, n, m) and grid[x][y]:
                    adjPos = (x * n) + y 
                    adjParents.add(ds.findPar(adjPos))
            currSum = 1 + sum([ds.size[parent] for parent in adjParents])
            res = max(res, currSum)

        return res
        

''' time complexity : O(n * m * 4 * alpha)
    space complexity : O(n * m)
'''

#################################################################################################################################################################################

# GFG editorial solution with DFS and modifying or using of input grid

from typing import List, Set
from collections import defaultdict


class Solution:
    #Function to perform depth-first search on grid.
    def dfs(self, grid: List[List[int]], i: int, j: int, index: int) -> int:
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        grid[i][j] = index
        count = self.dfs(grid, i + 1, j, index) + self.dfs(grid, i - 1, j, index) + \
                self.dfs(grid, i, j + 1, index) + self.dfs(grid, i, j - 1, index)
        return count + 1

    #Function to find neighbors of a cell in the grid.
    def findNeighbours(self, grid: List[List[int]], i: int, j: int,
                       s: Set[int]) -> None:
        n = len(grid)
        if i > 0:
            s.add(grid[i - 1][j])
        if j > 0:
            s.add(grid[i][j - 1])
        if i < n - 1:
            s.add(grid[i + 1][j])
        if j < n - 1:
            s.add(grid[i][j + 1])

    #Function to find maximum connections in the grid.
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        index = 2
        area = defaultdict(int)

        #Iterating over the grid to perform dfs on islands.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = self.dfs(grid, i, j, index)
                    res = max(res, area[index])
                    index += 1

        #Iterating over the grid to find maximum connections.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    self.findNeighbours(grid, i, j, s)
                    count = 1  # to account for the converted island
                    for val in s:
                        count += area[val]
                    res = max(res, count)

        return res


''' time complexity : O(n * m)
    space complexity : O(n * m)
'''
