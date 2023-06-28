# SOLUTION 1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # enter all of the numbers in nums into a dictionary
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = 1
        
        # go through the numbers in range 0 -> n inclusive
        # and find the missing number
        missing = 0
        for i in range(len(nums)+1):
            if i not in d:
                missing = i
                break
        
        return missing


# SOLUTION 2
    def missingNumber1(self, nums: List[int]) -> int:
        # find the sum of numbers in range 0 -> n inclusive
        sum_range = 0
        for i in range(len(nums)+1):
            sum_range += i

        # the difference between the two sums will be the missing number
        return sum_range - sum(nums)
