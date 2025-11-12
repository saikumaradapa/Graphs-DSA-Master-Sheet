problem link : https://www.geeksforgeeks.org/problems/word-ladder/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=word-ladder


from collections import deque
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        wordList = set(wordList)  # Ensure O(1) lookup
        if targetWord not in wordList:
            return 0
        
        q = deque([(startWord, 1)])
        visited = set([startWord])
        
        while q:
            w, step = q.popleft()
            if w == targetWord:
                return step
            for i in range(len(w)):
                for j in range(ord('a'), ord('z') + 1):
                    tempWord = w[:i] + chr(j) + w[i+1:]
                    if tempWord in wordList and tempWord not in visited:
                        q.append((tempWord, step+1))
                        visited.add(tempWord)
        return 0
        
''' BFS 
    time complexity : O( N * word.length * 26)        
    space complexity : O(n)
'''
