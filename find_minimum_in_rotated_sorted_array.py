class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use a binary search to solve this
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l + r) // 2  # find the middle point
            
            # compare the number at right and middle, if r < m that 
            # means the beginning of the numbers is on the right side
            if nums[r] < nums[mid]:
                l = mid + 1
            
            # if m < r then that means the smaller side is on the left
            else:
                r = mid

        return nums[l]

    
    # Time Complexity: O(logn), binary search
    # Space Complexity: O(1), pointer variables
