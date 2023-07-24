class Solution:

    # approach 1, faster but more space used
    def majorityElement1(self, nums: List[int]) -> int:
        majority = len(nums) // 2  # calculation for majority
        
        count = {}  # keep count of the numbers we have seen
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

            if count[num] > majority: return num

    # Time Complexity: O(n), traverse the array
    # Space Complexity: O(n), dictionary to keep track of the count


    # approach 2, slower but less space used
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]  # since majority, the number must be at the middle

    # Time Complexity: O(nlogn), built in python sort is around O(nlogn) on average
    # Space Complexity: O(1)
