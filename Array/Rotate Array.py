#Python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-k
        x=nums[:n]
        del nums[:n]
        nums.extend(x)
