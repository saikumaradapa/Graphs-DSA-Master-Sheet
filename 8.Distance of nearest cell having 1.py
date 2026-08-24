Problem Link1 : https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
Problem Link2 : https://leetcode.com/problems/01-matrix/description/

from collections import deque

class Solution:
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        dx = (0, -1, 0, 1, 0)
        while q:
            row, col = q.popleft()
            for i in range(4):
                r, c = row + dx[i], col + dx[i+1]
                if 0 <= r < n and 0 <= c < m and dist[r][c] == -1:
                    dist[r][c] = dist[row][col] + 1
                    q.append((r, c))

        return dist

            
''' BFS 
    time complexity : O(n*m)
    space complexity : O(n*m)
'''  
