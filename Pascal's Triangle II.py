class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #n = int(math.pow(11,rowIndex))
        #return [int(d) for d in str(n)]
        
        row = [1]
        
        for i in range(rowIndex):
            row  = [1] + [row[prev]+row[prev+1] for prev in range(len(row)-1)]+[1]
        return row
        
        
