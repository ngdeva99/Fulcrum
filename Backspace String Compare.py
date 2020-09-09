class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        print(S[0])
        
        stack = []
        
        for i in S:
            
            if i=="#":
                if len(stack)==0:
                    continue
                stack.pop()
            else:
                stack.append(i)
        S=""
        while len(stack)!=0:
            c = stack.pop(0)
            S+=str(c)
                
        print(S)
        
        for i in T:
            
            if i=="#":
                if len(stack)==0:
                    continue
                stack.pop()
            else:
                stack.append(i)
        T=""
        while len(stack)!=0:
            c = stack.pop(0)
            T+=str(c)
                
        print(T)
        
        return T==S
