class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        q = [int(d) for d in a]
        print(q)
        w = [int(d) for d in b]
        print(w)
        
        path = 0
        path1 = 0
        for c in q:
            path = 2*path + c
            
        for c in w:
            path1 = 2*path1+c
            
        return bin(path+path1)[2:]
