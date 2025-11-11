problem link : https://www.geeksforgeeks.org/problems/alien-dictionary/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=alien-dictionary

from collections import defaultdict, deque
class Solution:
    def findOrder(self, words):
        # Step 1: collect all unique letters
        unique_letters = set(''.join(words))
        graph = defaultdict(list)
        indegree = {ch:0 for ch in unique_letters}
        
        # Step 2: build the graph, handle prefix case
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # prefix check 
            # for test case like [abc, ab]
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
        
        # Step 3: Kahn's Algorithm for Topo Sort
        q = deque([ch for ch in unique_letters if indegree[ch] == 0])
        res = []
        
        while q:
            ch = q.popleft()
            res.append(ch)
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Step 4: check for cycles
        if len(res) != len(unique_letters):
            return ""

        return "".join(res)

''' BFS 
    time complexity : O(n * m)
    space complexity : O(n * m)
'''

