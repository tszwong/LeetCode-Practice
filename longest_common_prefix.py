class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs) # sorts the strings lexicographically
        res = ""

        first_str = strs[0]
        last_str = strs[-1]
        shortest = min(len(first_str), len(last_str))

        for i in range(shortest): # iterate until last letter of the shorter string
            if first_str[i] == last_str[i]: # update prefxi
                res += first_str[i]
            else: # when a letter does not match up
                return res
                
        return res

    
    # Time Complexity: O(n), traverse the chars of a string
    # Space Complexity: O(1)
