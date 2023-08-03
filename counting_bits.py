class Solution:

    # dynamic programming problem
    def countBits(self, n: int) -> List[int]:
        res = [0]  # initializing the list to hold the results

        for i in range(1, n+1):  # since we want it to be inclusive from 1 to n
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i // 2] + 1) # add back the trailing bit

        return res


    # Time Complexity: O(n), we need to count the 1's in the binary representing of each number from 1 -> n
    # Space Complexity: O(n), array to hold results
