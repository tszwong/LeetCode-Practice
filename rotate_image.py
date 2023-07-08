class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # reverse the matrix
            # matrix.reverse() using built-in function
        # without using built-in function
        l = 0 
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # transpose i.e. interchanging the rows with the columns of each entry
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
