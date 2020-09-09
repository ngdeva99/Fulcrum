class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i,j=0,0
        
        
        if not all(nums1[i] <= nums1[i+1] for i in range(len(nums1) - 1)):
            nums1 = sorted(nums1)
            
        if not all(nums2[i] <= nums2[i+1] for i in range(len(nums2) - 1)):
            nums2 = sorted(nums2)
            
        while i<len(nums1) and j<len(nums2):
                
            diff = nums1[i]-nums2[j]
            
            if diff==0:
                res.append(nums1[i])
                i+=1
                j+=1
             
            elif diff<0:
                i+=1
                
            else:
                j+=1
                
        return res
                    
                    
            
            
            
            
        
        
