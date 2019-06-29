

class UnionFind(object):
    def __init__(self, n):
        self.u = list(range(n))
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.u[ra] = rb
    def find(self, a):
        while self.u[a] != a:
            a = self.u[a]
        return a

class Solution(object):
    def findCircleNum(self, M):
        if not M:
            return 0
        s = len(M)
        uf = UnionFind(s)
        for r in range(s):
            for c in range(r, s):
                if M[r][c] == 1:
                    uf.union(r, c)
        return len(set([uf.find(i) for i in range(s)]))


'''
Ideas/thoughts:
sanity check is ,if len is empty, just return 0 friend groups.
Iterating thru the each person frnd list, go to check upto len of frnd list , It would be  a square matrix.
The two important functions union and find, union will add elements and find will check element.
'''