class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window problem
        res = 0
        count = {}  # track the frequency of characters in the string

        l = 0  # left pointer
        for r in range(len(s)):  # right pointer will move until end of str
            # get character from the hashmap, if it doesn't exist default value = 0
            count[s[r]] = 1 + count.get(s[r], 0) 

            while (r-l+1) - max(count.values()) > k:  # length of window - most frequent value
                count[s[l]] -= 1  # decrement character count
                l += 1  # shift left pointer since we cannot make > k replacements

            res = max(res, r-l+1)  # update if greater than current max

        return res


  # Time Complexity: O(n), traverse string once
  # Space Complexity: O(1) with worst case being O(m) where m is the number of elements in hashmap for the characters


  # with optimization
  def characterReplacement(self, s: str, k: int) -> int:
        # sliding window problem
        res = 0
        count = {}  # track the frequency of characters in the string
        most_frequent = 0

        l = 0  # left pointer
        for r in range(len(s)):  # right pointer will move until end of str
            # get character from the hashmap, if it doesn't exist default value = 0
            count[s[r]] = 1 + count.get(s[r], 0) 
            most_frequent = max(most_frequent, count[s[r]])

            while (r-l+1) - max(count.values()) > k:  # length of window - most frequent value
                count[s[l]] -= 1  # decrement character count
                l += 1  # shift left pointer since we cannot make > k replacements

            res = max(res, r-l+1)  # update if greater than current max

        return res
