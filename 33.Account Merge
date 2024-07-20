Problem Link : https://www.geeksforgeeks.org/problems/account-merge/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=account-merge

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n 
        self.count = n 
    
    def findPar(self, node):
        if node == self.parent[node]:
            return node 
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        up_u = self.findPar(u)
        up_v = self.findPar(v)
        if up_u == up_v:
            return 
    
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_u] += self.size[up_v]
        else :
            self.parent[up_v] = up_u
            self.size[up_v] += self.size[up_u]
        self.count -= 1

class Solution:
    def accountsMerge(self, accounts):
        hasMap = dict()
        ds = DisjointSet(len(accounts))
        for i in range(len(accounts)) :
            for j in range(1, len(accounts[i])) :
                if accounts[i][j] in hasMap :
                    ds.union(i, hasMap[accounts[i][j]])
                else :
                    hasMap[accounts[i][j]] = i 
        
        mergedMail = [[] for i in range(len(accounts))]
        
        for mail, idx in hasMap.items():
            mergedMail[ds.findPar(idx)].append(mail)
        
        res = []
        
        for idx, mail in enumerate(mergedMail):
            temp = sorted(mergedMail[idx])
            if temp :
                temp = [accounts[idx][0]] + temp
                res.append(temp)
        return res
                
''' time complexity : O(n * m * 4 alpha)
    space complexity : O(n)
'''
