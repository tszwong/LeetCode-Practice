class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # pointers
        l = 0
        r = len(nums)-1
        curr = 0

        while curr <= r:
            if nums[curr] == 0: # move all 0's to the left
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                curr += 1

            elif nums[curr] == 2: # move all the 2's to the right
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            
            else:  # don't do anything to the 1's
                curr += 1


    # Time Complexity: O(n), we traverse the array once
    # Space Complexity: O(1), pointer variables
