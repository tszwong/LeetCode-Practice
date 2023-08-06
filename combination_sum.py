class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # create a list for storing the result

    
        def dfs(index, curr, total): # helper function for dfs
            if total == target:  # base case
                res.append(curr.copy())  # add the current combination sum to res
                # since lists are mutable, we use copy() to add the current instance of curr
                return
        
            if index >= len(candidates) or total > target:  # not a valid combination
                return
                
            curr.append(candidates[index])  # add to curr if neither base cases were met
            dfs(index, curr, total+candidates[index])  # make recursive call with updated sum
            curr.pop()  # remove the last element of curr, backtrack
            dfs(index+1, curr, total)  # move to next candidate and try another combination
            

        dfs(0, [], 0)  # call the helper function to initiate dfs
        return res

      
  # Time Complexity: O(2^n), each recursive call can have 2 possibilities worst case
  # Space Complexity: O(2^n), at worst case there are 2^n possible combinations to be stored in res
