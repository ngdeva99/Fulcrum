class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftptr = 0
        rtptr = len(numbers)-1
        
        while leftptr < rtptr:
            
            calc = numbers[leftptr]+numbers[rtptr]
            
            if calc == target:
                
                return [leftptr+1,rtptr+1]
            
            elif calc<target:
                
                leftptr = leftptr + 1
            
            elif calc>target:
                rtptr = rtptr - 1
                
        return []
