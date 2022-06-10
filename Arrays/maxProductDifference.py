class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        max1 = nums[-1]
        max2 = nums[-2]
        min1 = nums[0]
        min2 = nums[1]
        
        return (max1*max2) - (min1*min2)
        
