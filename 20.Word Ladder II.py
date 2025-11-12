problem link : https://www.geeksforgeeks.org/problems/word-ladder-ii/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=word-ladder-ii



from collections import deque

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        wordSet = set(wordList)
        q = deque([[startWord]])
        
        if startWord in wordSet:
            wordSet.remove(startWord)
        
        minLen = None 
        res = []
        
        while q:
            n = len(q)
            removeWords = set()
            
            for _ in range(n):
                wordArr = q.popleft()
                step = len(wordArr)
                
                if minLen and step > minLen:
                    continue
                
                if wordArr[-1] == targetWord:
                    res.append(wordArr.copy())
                    minLen = step 
                
                word = list(wordArr[-1])
                temp = word[:]
                    
                for i in range(len(word)):
                    for j in range(26):
                        temp[i] = chr(j + ord('a'))
                        
                        newWord = ''.join(temp)
                        if newWord in wordSet:
                            q.append(wordArr + [newWord])
                            removeWords.add(newWord)
                    temp = word[:]
                    
            for word in removeWords:
                wordSet.remove(word)
        
        return res

''' time complexity : O(L * N * M * 26) - L number of paths
    space complexity : O(L * N * M)
'''




######################################################################################################################################################

# for large value n

def findSequences(startWord, targetWord, wordList):
    wordList = set(wordList)
    if targetWord not in wordList:
        return []

    distances = {startWord: 0}
    graph = collections.defaultdict(list)
    queue = deque([startWord])

    while queue:
        word = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    graph[word].append(next_word)
                    if next_word not in distances:
                        distances[next_word] = distances[word] + 1
                        queue.append(next_word)

    res = []
    path = [startWord]

    def dfs(word):
        if word == targetWord:
            res.append(path[:])
            return
        for next_word in graph[word]:
            if distances.get(next_word, float('inf')) == distances[word] + 1:
                path.append(next_word)
                dfs(next_word)
                path.pop()

    dfs(startWord)
    return res

 
''' time complexity : O(N * M * 26 + S * N) 
    space complexity : O(N^2 + S * N * M)
'''

