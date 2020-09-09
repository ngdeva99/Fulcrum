class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #using sets:
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1)<len(nums2):
            return self.inter(nums1,nums2)
        
        else:
            return self.inter(nums2,nums1)
        
    def inter(self,set1,set2):
        return [x for x in set1 if x in set2]
