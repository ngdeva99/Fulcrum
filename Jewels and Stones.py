class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        
        num = {}
        
        for x in J:
            if x in num:
                num[x]+=1
            else:
                num[x]=1
        ways =0
        for x in S:
            if x in num:
                ways+=1
            else:
                continue
        return ways
