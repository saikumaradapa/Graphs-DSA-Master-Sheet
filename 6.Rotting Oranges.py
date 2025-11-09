1. https://leetcode.com/problems/rotting-oranges/description/
2. https://www.geeksforgeeks.org/problems/rotten-oranges2536/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotten_oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        
        fresh_oranges = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        if fresh_oranges == 0:
            return 0
        
        x = (0, -1, 0, 1, 0)
        time = 0 
        while q:
            flag = False 
            for _ in range(len(q)):
                row, col = q.popleft()
                for i in range(4):
                    new_row, new_col = row + x[i], col + x[i+1]
                    if 0<=new_row<n and 0<=new_col<m and grid[new_row][new_col] == 1:
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        flag = True
                        fresh_oranges -= 1
            if flag:
                time += 1
        
        if fresh_oranges != 0:
            return -1
        return time 
                
''' time complexity : O(n*m)            BFS
    space complexity : O(n*m)
'''
