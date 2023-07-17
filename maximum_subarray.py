class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0  # if given empty list
        
        max_sum = curr_sum = nums[0] # itialize

        for i in range(1, len(nums)):
            # compare curr element with sum of curr element and curr sum
            curr_sum = max(curr_sum + nums[i], nums[i])

            # compare curr sum with max sum
            max_sum = max(max_sum, curr_sum)

        return max_sum


    # Time Complexity: O(n), we traverse the array once
    # Space Complexity: O(1), variables to hold sums
