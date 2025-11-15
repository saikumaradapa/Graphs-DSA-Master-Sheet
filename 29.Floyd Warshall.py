problem link : https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-floyd-warshall

class Solution:
	def floydWarshall(self, dist):
		res = dist.copy()
		n = len(dist)
		
		for via in range(n):
    		for i in range(n):
    		    for j in range(n):
    		        if res[i][via] != 10**8 and res[via][j] != 10**8:
                        res[i][j] = min(res[i][j], res[i][via] + res[via][j])
        return res
        
''' time complexity : O(n ^ 3)
    sapce complexity : O(n^2) 
'''

