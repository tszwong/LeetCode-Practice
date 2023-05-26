class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        left = 0
        right = 0
        max_len = 0

        # we will store the characters we have seen here with its index
        c = {}
        
        while right < len(s): # go through entire string
            if s[right] in c and c[s[right]] >= left:
                left = c[s[right]] + 1 # update left pointer
            
            # update values
            max_len = max(max_len, right - left + 1) 
            c[s[right]] = right # store new character and its index
            right += 1

        return max_len
