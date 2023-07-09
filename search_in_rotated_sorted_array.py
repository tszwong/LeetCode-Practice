class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Solution 1, O(n)
        #
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #
        # return -1


        # Solution 2, 2 pointer approach without using binary searcg
        # l = 0
        # r = len(nums)-1
        #
        # while l <= r:
        #     if nums[l] == target:
        #         return l
        #     elif nums[r] == target:
        #         return r
        #   
        #     l += 1  # update pointers
        #     r -= 1
        #
        # return -1


        # Solution 3, binary search O(logn) approach
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target: return mid # target found

            if nums[l] <= nums[mid]: # check if the left side is sorted
                if nums[l] <= target < nums[mid]: # check if target in left half
                    r = mid - 1
                else: # check right half since not in left half
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]: # check if target in right half
                    l = mid + 1
                else: # check left half since not in right half
                    r = mid - 1

        return -1 # not found
