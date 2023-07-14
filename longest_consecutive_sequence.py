class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set() # use a set to keep track of what numbers exist
        for num in nums:
            a.add(num)

        res = 0 # result

        for num in nums: # iterate throught the list of numbers

            curr = 1 # use a temp variable to track current sequence length
            if num-1 not in a: # new sequence

                while num+1 in a: # check if the current number +1 is in the list
                    num += 1
                    curr += 1

                res = max(res, curr) # update result

        return res


    # Time Complexity: O(n)
    # Space Complexity: O(n)
