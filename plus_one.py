class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # turn the array into a str
        str_digits = ""
        for digit in digits:
            str_digits += str(digit)
        
        # turn str into an int and add 1
        int_digits = int(str_digits) + 1
        # update str with new int value
        str_digits = str(int_digits)

        # now create a list and add each item back
        digits = [int(str_digits[i]) for i in range(len(str_digits))]

        return digits


    # Time Complexity: O(n), we traverse the list of n elements
    # Space Complexity: O(n), we replace digits with a new list with n elements
