class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.hamming_weight(x), x))
    
    @staticmethod
    def hamming_weight(num: int) -> int:
        #brian kersingan
        weight = 0

        while num>0:
            weight += num&1
            num>>=1

        return weight
        
