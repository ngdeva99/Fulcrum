class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        candidates=[0]*n
        for i in range (n):
            candidates[i] = (i + 1)
        fact=[-1]*(n + 1)
        fact[0] = 1;
        for i in range (1,n):
            fact[i] = fact[i - 1] * i
        k-=1
        for i in range (n-1,-1,-1):
            idx = k //fact[i]
            ans += str(candidates[idx])
            for j in range (idx,len(candidates)-1):

                candidates[j] = candidates[j + 1]
                
            k -= idx * fact[i]
        return ans
