Problem Link1 : https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
Problem Link2 : https://leetcode.com/problems/01-matrix/description/

from collections import deque 
class Solution:
	def nearest(self, grid):
		n, m = len(grid), len(grid[0])
	    n, m = len(grid), len(grid[0])
        visited = [[-1] * m for _ in range(n)] 
        
        q = deque([])

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append((i, j, 0))
                    
        dx = (0, -1, 0, 1, 0)
        
        while q:
            row, col, dist = q.popleft()
            if visited[row][col] == -1:
                visited[row][col] = dist 
                
                for i in range(4):
                    newRow, newCol = row + dx[i], col + dx[i+1]
                    
                    if self.valid(n, m, newRow, newCol) and visited[newRow][newCol] == -1:
                        q.append((newRow, newCol, dist+1))
                        
        return visited
        
    def valid(self, n, m, r, c):
        if 0<= r < n and 0<= c < m: return True 

            
''' BFS 
    time complexity : O(n*m)
    space complexity : O(n*m)
'''  
