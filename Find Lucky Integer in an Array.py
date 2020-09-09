class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        
        m = {}
        for i in arr:
            if i in m:
                
                m[i]+=1
            else:
                m[i]=1
                
                
        a = set(arr)
        n = []
        print(a)
        for i in a:
            print(i,i in m,i==m[i])
            if i in m and i==m[i]:
                n.append(i)
            else:
                continue
        return max(n) if len(n)>0 else -1 
