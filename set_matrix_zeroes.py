class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # finding the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # to track rows and columns that need to be changed
        row_mark = {}
        col_mark = {}
        # check if the current index contains a zero
        # then marking the rows and cols as needed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_mark[r] = True
                    col_mark[c] = True

        # changing the rows and cols we marked to 0s
        for r in range(rows):
            for c in range(cols):
                if r in row_mark or c in col_mark:
                    matrix[r][c] = 0

        # time complexity = O(n^2) because of the nested loops
        # space complexity = O(m + n) because of two dictionaries
