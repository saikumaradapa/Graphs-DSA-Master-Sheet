problem link:  https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=flood-fill-algorithm

from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    n, m = len(image), len(image[0])
	    srcColor = image[sr][sc]
	    visited = [[0] * m for _ in range(n)]
	    x = (0, -1, 0, 1, 0)
	    
	    q = deque([(sr, sc)])	    
	    while q:
	        row, col = q.popleft()

            image[row][col] = newColor
            visited[row][col] = 1 
            
            for i in range(4):
                newRow, newCol = row + x[i], col + x[i+1]
                
                if 0<= newRow < n and 0<= newCol < m and image[newRow][newCol] == srcColor and not visited[newRow][newCol]:
                    q.append((newRow, newCol))
	                    
	    return image


''' time complexity : O(n * m)
    space complexity : O(n * m)
'''
