problem link : https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1


from collections import deque
from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        if not grid[source[0]][source[1]] or not grid[destination[0]][destination[1]]:
            return -1
        
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        
        dx = (0, -1, 0, 1, 0)
        q = deque([(0, source[0], source[1])])
        while q:
            d, row, col = q.popleft()
            if row == destination[0] and col == destination[1]:
                return d
            
            visited[row][col] = 1
            for i in range(4):
                newRow, newCol = row+dx[i], col+dx[i+1]
                if 0<=newRow<n and 0<=newCol<m and not visited[newRow][newCol] and grid[newRow][newCol]:
                    q.append((d+1, newRow, newCol))
        return -1
        
''' 
    time complexity : O(n * m)
    space complexity : O(n * m)
    
    can be solve with Dijkstra Algorithm with addition log time complexity for heap/pq 
'''        


#####################################################################################################################################################


from heapq import heapify, heappush, heappop
from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        if not grid[source[0]][source[1]] or not grid[destination[0]][destination[1]]: 
            return -1 
        
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        
        heap = [(0, source[0], source[1])] # dist, r, c 
        dx = (0, -1, 0, 1, 0)
        while heap:
            dist, row, col = heappop(heap)
            if row == destination[0] and col == destination[1]: 
                return dist 
            
            visited[row][col] = 1 
            
            for i in range(4):
                newRow, newCol = row + dx[i], col + dx[i+1]
                if 0<= newRow < n and 0<= newCol < m and not visited[newRow][newCol] and grid[newRow][newCol]:
                    heappush(heap, (dist+1, newRow, newCol))
                    visited[newRow][newCol] = 1
        return -1



''' time complexity : O(nm log nm)
    space complexity : O(n * m)
'''        
