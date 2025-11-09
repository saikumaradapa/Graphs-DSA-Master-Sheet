problem link : https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=replace-os-with-xs

class Solution:
    def fill(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == "O" and not visited[i][j]:
                    self.dfs(i, j, grid, visited, n, m)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "O":
                    grid[i][j] = "X"
        
    def dfs(self, i, j, grid, visited, n, m):
        if 0<=i<n and 0<=j<m and not visited[i][j] and grid[i][j] == "O": 
            visited[i][j] = 1
            self.dfs(i-1, j, grid, visited, n, m)
            self.dfs(i, j-1, grid, visited, n, m)
            self.dfs(i+1, j, grid, visited, n, m)
            self.dfs(i, j+1, grid, visited, n, m)

''' DFS
    time complexity : O(n*m)
    space complexity : O(n*m)
'''

#########################################################################################################################################################


from collections import deque
class Solution:
    def fill(self, n, m, mat):
        visited = [[0] * m for _ in range(n)]
        q = deque([])
        
        for c in range(m):
            if mat[0][c] == 'O':
                q.append((0, c))
            if mat[n-1][c] == 'O':
                q.append((n-1, c))
        
        for r in range(n):
            if mat[r][0] == 'O':
                q.append((r, 0))
            if mat[r][m-1] == 'O':
                q.append((r, m-1))
               
               
        dx = (0, -1, 0, 1, 0)                
        while q:
            row, col = q.popleft()
            
            if not visited[row][col]:
                visited[row][col] = 1
                
                for i in range(4):
                    nr, nc = row + dx[i], col + dx[i+1]
                    if self.valid(n, m, nr, nc) and mat[nr][nc] == 'O' and not visited[nr][nc] :
                        q.append((nr, nc))
        
        res = [['X'] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    res[i][j] = 'O'
        
        return res
                        
                    
    def valid(self, n, m, r, c):
        if 0<= r < n and 0<= c < m: return True 

        

''' BFS
    time complexity : O(n*m)
    space complexity : O(n*m)
'''

