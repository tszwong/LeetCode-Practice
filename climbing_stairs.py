class Solution:
    def climbStairs(self, n: int) -> int:  # bottom-up Dynamic Programming approach
        
        x = 1  # variables to hold the last two values
        y = 1

        for i in range(n-1):
            temp = x  # temporary variable to hold the value of x
            x = x + y  # update x with itself and the number behind it 
            y = temp  # update y with the number before it held in the temp variable

        return x


    # Time Complexity: O(n), we find the number of ways to climb n steps
    # Space Complexity: O(1), temporary variables to hold values of the two most recent values
