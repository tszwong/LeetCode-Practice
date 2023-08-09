class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0  # counter to keep track of palindromic substrings

        # expand from center approach
        for i in range(len(s)):

            # pointers, when the center is the same character
            left = i
            right = i

            # run while within boundaries and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        
            # pointers, when the left and right start from two 
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1


        return count


    # Time Complexity: O(n^2), we expand from each character of the string
    # Space Complexity: O(1), variables for counter and pointers
