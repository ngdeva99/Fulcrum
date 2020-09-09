class Solution:
    def tribonacci(self, N: int) -> int:
        
        if N==0:
            return 0
        if N==1:
            return 1
        if N==2:
            return 1
        fib1 = []
        fib1.append(0)
        fib1.append(1)
        fib1.append(1)
        
        for i in range(3,N+1):
            fib1.append(fib1[i-1] + fib1[i-2]+fib1[i-3])
        
        print(fib1)
        return fib1.pop()
