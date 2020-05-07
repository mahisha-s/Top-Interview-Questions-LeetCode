#Python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(digits[i]) for i in range(0,len(digits))]
        n=str(int(''.join(digits))+1)
        return list(map(int,n))
        
        
