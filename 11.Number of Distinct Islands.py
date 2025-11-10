problem link : https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-distinct-islands

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        set_of_unique_islands = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    curr_island = []
                    self.dfs(i, j, grid, visited, n, m, i, j, curr_island)
                    set_of_unique_islands.add(tuple(curr_island))
        return len(set_of_unique_islands)
        
    def dfs(self, r, c, grid, visited, n, m, r0, c0, curr_island):
        if 0<=r<n and 0<=c<m and grid[r][c] and not visited[r][c]:
            curr_island.append((r-r0, c-c0))
            visited[r][c] = 1
            self.dfs(r, c+1, grid, visited, n, m, r0, c0, curr_island)
            self.dfs(r+1, c, grid, visited, n, m, r0, c0, curr_island)
            self.dfs(r, c-1, grid, visited, n, m, r0, c0, curr_island)
            self.dfs(r-1, c, grid, visited, n, m, r0, c0, curr_island)

''' DFS
    time complexity : O(n*m)
    space complexity : O(n*m)
'''
            
#######################################################################################################################################################

from collections import deque
import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] *m for _ in range(n)]
        s = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    s.add(self.bfs((i, j), (i, j), visited, grid, n, m))
        return len(s)
    
    def bfs(self, curr, start, visited, grid, n, m):
        land = []
        dx = (0, -1, 0, 1, 0)
        q = deque([curr])
        
        while q:
            row, col = q.popleft()
            if not visited[row][col]:
                visited[row][col] = 1
                land.append((row-start[0], col-start[1]))
                
                for i in range(4):
                    nr, nc = row + dx[i], col + dx[i+1]
                    if self.valid(n, m, nr, nc) and grid[nr][nc] == 1 and not visited[nr][nc] :
                        q.append((nr, nc))
        return tuple(land)

    def valid(self, n, m, r, c):
        if 0<= r < n and 0<= c < m: return True   


''' BFS
    time complexity : O(n*m)
    space complexity : O(n*m)
'''

