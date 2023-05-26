class Solution:
    def isPalindrome(self, x: int) -> bool:
        # we can turn the int into a string
        str_x = str(x)
        # check if the string is equal to its reverse
        return str_x == str_x[::-1]
