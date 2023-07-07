class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # result array

        pre = 1  # left side of array
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1  # right side of array
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
