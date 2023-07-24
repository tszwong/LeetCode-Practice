class Solution:

    # Approach 1
    def removeDuplicates1(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))  # set ignores duplicates, [:] allows for in-place
        return len(nums)  # since every element is now unique, we can just return the length

    # Time Complexity: O(nlogn), using built in sorting functions
    # Space Complexity: O(n), creating a set from nums


    # Approach 2
    def removeDuplicates2(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        
