class UnionFind(object):
    def __init__(self):
        self.u = list(range(1001))

    def union(self,a,b):
        ra,rb = self.find(a),self.find(b)
        if ra!=rb:
            #making the associatoion
            self.u[ra]=rb
            return False
        return True
    
    def find(self,a):
        while self.u[a]!=a:
            a=self.u[a]
        
        return a
    
    def p(self):
        return self.u

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind()
        for edge in edges:
            if uf.union(*edge):
                return edge
