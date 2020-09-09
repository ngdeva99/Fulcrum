class Solution:
    def searchMatrix(self, matrix, target):
        

        for row in matrix:
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]>target:
                    end = mid
                elif row[mid]<target:
                    start = mid+1
                else:
                    return True
            continue
            
        return False
