class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        
        x1 = coordinates[0][0]
        y1 = coordinates [0][1]
        
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        x3=1
        if x1==x2:
            x3 = 0
        else:
            
            slope = (y2-y1)/(x2-x1)
        
        #eqn = y-y1-(m*(x-x1))
        
        for i in range(2,len(coordinates)-1):
            if x3==1:
                
                if coordinates[i][1]-y1-(slope*(coordinates[i][0]-x1))!=0:
                    return False
            else:
                if coordinates[i][0]!=x1:
                    return False
        return True
        
