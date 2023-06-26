class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {} # keep track of numbers we have seen so far

        for i in range(len(nums)):
            if nums[i] not in appeared: # add if new
                appeared[nums[i]] = 1
            else:
                return True

        return False
        
