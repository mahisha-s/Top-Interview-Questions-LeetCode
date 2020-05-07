#Python3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        if(len(nums1)<len(nums2)):
            for i in nums1:
                if(i in nums2):
                    x+=[i]
                    nums2.remove(i)
        else:
            for i in nums2:
                if(i in nums1):
                    x+=[i]
                    nums1.remove(i)
        return x
            
        
