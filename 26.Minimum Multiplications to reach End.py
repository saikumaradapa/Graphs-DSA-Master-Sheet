problem link : https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimum-multiplications-to-reach-end


from collections import deque 
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        cost = [float('inf')] * 100000
        cost[start] = 0
        q = deque([(start, 0)]) # mul, steps
        
        while q:
            mul, steps = q.popleft()
            
            for num in arr:
                curr = (num * mul) % 100000
                if cost[curr] > steps + 1:
                    cost[curr] = steps + 1
                    if curr == end: 
                        return cost[curr]
                    q.append((curr, steps+1))
        
        return cost[end] if cost[end] != float('inf') else -1
        
        
''' time complexity : O(100000 * N)
    space complexity : O(100000)
'''
