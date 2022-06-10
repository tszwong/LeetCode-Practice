class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        
        values = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in values:
                return [i,values.get(nums[i])]
            else:
                values[diff] = i
              
