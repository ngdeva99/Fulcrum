class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        
        time = 0
        visited = set()
        queue,new_queue = [],[]
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                    
        while len(queue)!=0:
            
            curr = queue.pop(0)
            visited.add(curr)
            
            for dir in dirs:
                
                new_row = curr[0]+ dir[0]
                new_col = curr[1]+dir[1]
            
                if ((0<=new_row<row) and (0<=new_col<col) and ((new_row,new_col) not in visited) and 
                    (grid[new_row][new_col]==1)):
                    
                    grid[new_row][new_col] = 2
                    visited.add((new_row,new_col))
                    new_queue.append((new_row,new_col))
                    
            if len(queue)==0 and len(new_queue)>0:
                time+=1
                queue = new_queue
                new_queue = []
                
                
        ###################
        print(grid)
        for i in range(row):
            for j in range(col):
                ######## final check if any fresh orange is present
                if grid[i][j]==1:
                    return -1
        
        return time
        
