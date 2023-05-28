class Solution:
    def isPalindrome(self, s: str) -> bool:

        # change the string to lower case
        s = s.lower()
        new_s = ""
        # remove all non-alphanumeric characters
        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i]

        # approach 1, two pointers approach O(n)
        # l = 0  # front
        # r = len(new_s)-1  # back

        # while l < r:
        #     if new_s[l] == new_s[r]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False

        # return True

        # approach 2, slicing O(n)
        return new_s == new_s[::-1]
