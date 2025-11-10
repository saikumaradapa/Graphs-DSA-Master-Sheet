problem link : https://www.geeksforgeeks.org/problems/number-of-enclaves/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-enclaves        

from collections import deque
from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        q = deque([])
        
        for c in range(m):
            if grid[0][c] == 1:
                q.append((0, c))
            if grid[n-1][c] == 1:
                q.append((n-1, c))
        
        for r in range(n):
            if grid[r][0] == 1:
                q.append((r, 0))
            if grid[r][m-1] == 1:
                q.append((r, m-1))
                
        dx = (0, -1, 0, 1, 0)                 
        while q:
            row, col = q.popleft()
            if not visited[row][col] :
                visited[row][col] = 1
                
                for i in range(4):
                    nr, nc = row + dx[i], col + dx[i+1]
                    if self.valid(n, m, nr, nc) and grid[nr][nc] == 1 and not visited[nr][nc] :
                        q.append((nr, nc))     
        res = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    res += 1
        return res
        
    def valid(self, n, m, r, c):
        if 0<= r < n and 0<= c < m: return True 

''' time complexity : O(n*m)
    space complexity : O(n*m)
'''
