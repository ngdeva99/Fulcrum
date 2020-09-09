class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        
        traverse=[]
        
        direction='U'
        
        x=0
        y=0
        
        traverse.append(matrix[x][y])
        
        while x!=len(matrix)-1 or y!=len(matrix[0])-1:
            
            
            while direction=='U':
                
                if x==0 or y==len(matrix[0])-1:
                    if x==0 and y!=len(matrix[0])-1:
                        y=y+1
                    
                    else:
                        x=x+1
                
                    direction='D'
                
                else:
                    x=x-1
                    y=y+1
                
                traverse.append(matrix[x][y])
                
                if x==len(matrix)-1 and y==len(matrix[0])-1:
                    return traverse
            
            while direction=='D':
                
                if x==len(matrix)-1 or y==0:
                    if x!=len(matrix)-1 and y==0:
                        x=x+1
                        
                    else:
                        y=y+1
                
                    
                    direction='U'
                
                else:
                    x=x+1
                    y=y-1
                
                traverse.append(matrix[x][y])
                
                if x==len(matrix)-1 and y==len(matrix[0])-1:
                    return traverse
        
        return traverse
        
