class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0

        # binary search approach

        # initialize pointers
        l = m = 0
        r = len(nums)-1
        
        # cases where the target is outside of nums
        if nums[0] > target: return 0
        elif nums[-1] < target: return len(nums)
        
        while l <= r:  # search until pointers l and r pass each other
            m = (l + r) // 2
            if nums[m] == target: # found target
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l # insert position since target not found

    
    # Time Complexity: O(logn), binary search
    # Space Complexity: O(1), pointer variables
