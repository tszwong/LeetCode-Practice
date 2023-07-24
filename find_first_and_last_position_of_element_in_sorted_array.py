class Solution:
    # wrapper function
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []: return [-1, -1] # edge case

        # use helper functions to find each of the bounds
        low = self.find_left_index(nums, target)
        high = self.find_right_index(nums, target)

        # put the two results in a list
        res = [low, high]
        return res

    # Time Complexity: O(logn), binary search
    # Space Complexity: O(1)


    # helper function to find the lower end of the range
    def find_left_index(self, nums, target):
        i = -1  # base value is -1 in case we don't find the number in the array
        l = 0
        r = len(nums)-1

        # utilize binary search
        while l <= r:
            m = (l + r) // 2  # find middle point

            if nums[m] == target:
                i = m  # update found index
                r = m - 1  # see if any other target on the left i.e. smaller index than the one we just found
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return i

        

    # helper function to find the upper end of the range
    def find_right_index(self, nums, target):
        i = -1
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                i = m
                l = m + 1  # see if there's any other target on right i.e. larger index than the one we just found
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return i
