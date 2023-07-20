class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            
            # odd length case
            l, r = i, i  # setting pointers, starting from current index which we treat as the "center" character
            while l >= 0 and r < len(s) and s[l] == s[r]: # check boundaries and if chars match
            
                if (r - l + 1) > res_len: # if the current length is greater than the max
                    res = s[l:r+1]  # update the string
                    res_len = r - l + 1  # update the max length

                # update pointers, i.e. expand left and right pointers from current index
                l -= 1
                r += 1

            # basically same thing but for even length case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
            
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                l -= 1
                r += 1
        
        return res

      
  # Time Complexity: O(n^2), nested loop to check character combinations
  # Space Complexity: O(1), pointers, result variables
