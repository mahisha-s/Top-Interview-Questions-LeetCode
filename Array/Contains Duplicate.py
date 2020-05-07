#Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        s=list(set(nums))
        s.sort()
        if(s==nums):
            return False
        else:
            return True
        
