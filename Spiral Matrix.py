class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix)==0:
            return []
        
        direction = 'R'
        
        r,c = len(matrix),len(matrix[0])
        count = 0
        
        traverse = []
        
        i,j = 0,0
        while count<(r*c):
            
            while direction == 'R':
                
                if j==c or matrix[i][j] == float('inf'):
                    direction = 'D'
                    break
                else:

                    traverse.append(matrix[i][j])
                    matrix[i][j] = float('inf')
                    count+=1
                    j+=1

                    if count==(r*c):
                        return traverse

                
            i+=1
            j-=1
            
            
            while direction == 'D' :
                
                if i==r or matrix[i][j] == float('inf'):
                    direction = 'L'
                    break
                else:

                    traverse.append(matrix[i][j])
                    matrix[i][j] = float('inf')
                    count+=1
                    i+=1

                    if count==(r*c):
                        return traverse
            i-=1
            j-=1
            
            while direction == 'L':
                
                if j==-1 or matrix[i][j] == float('inf'):
                    direction = 'U'
                    break
                else:

                    traverse.append(matrix[i][j])
                    matrix[i][j] = float('inf')
                    count+=1
                    j-=1

                    if count==(r*c):
                        return traverse
                
            
            i-=1
            j+=1
            
            while direction == 'U' :
                
                if i==-1 or matrix[i][j] == float('inf'):
                    direction = 'R'
                    break
                    
                else:     
                    traverse.append(matrix[i][j])
                    matrix[i][j] = float('inf')
                    count+=1
                    i-=1


                    if count==(r*c):
                        return traverse
                
            i+=1
            j+=1
                
            
        
        return traverse
            
        
