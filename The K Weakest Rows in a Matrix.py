class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        def bin(row):
            
            
            #for handling n=2 also len(row) otherwise it would have been len(row)-1
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]==0:
                    end = mid
                else:
                    start = mid+1
            return len(row)- start
        
        count = 0
        res ={}
        for row in mat:
            res[count]=len(row)-bin(row)
            count +=1
            
        res = sorted(res.items(), key = lambda kv:(kv[1], kv[0]))  
        print(res)
        res = [res[i][0] for i in range(k)]
        return res
