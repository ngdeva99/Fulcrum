class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #DUTCH PARTIONING ALGORITHM
        
        
        arr_size = len(a)
        lo = 0
        hi = arr_size - 1
        mid = 0
        while mid <= hi: 
            if a[mid] == 0: 
                a[lo], a[mid] = a[mid], a[lo] 
                lo = lo + 1
                mid = mid + 1
            elif a[mid] == 1: 
                mid = mid + 1
            else: 
                a[mid], a[hi] = a[hi], a[mid]  
                hi = hi - 1

