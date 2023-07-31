class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []  # edge caseggg

        digits_char = {  # map the characters to the number
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        # have helper function inside so we don't need to pass in parameters
        # from the outer function everytime
        def backtrack(index, curr):
            if len(curr) == len(digits):  # base case, we finished building the string
                res.append(curr)
                return

            for char in digits_char[digits[index]]:  # recursive case
                backtrack(index+1, curr+char)

        # call the backtrack function
        backtrack(0, "")

        return res


    # Time Complexity: O(4^n), we make at most 4 recursive calls for each digit of the characters in the hashmap
    # Space Complexity: O(n + 4^n), space used during recursive calls = n and the space used to store the result is 4^n
