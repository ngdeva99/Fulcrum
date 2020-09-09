class Solution:
    def maximumGap(self, num: List[int]) -> int:
        
        
        ##BUCKET SORT
        
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = (b-a)//(len(num)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        print(bucket)
        for n in num:
            b = bucket[(n-a)//size]
            
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
            print(b)
        bucket = [b for b in bucket if b[0] is not None]
        print(bucket)
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))
