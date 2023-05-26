class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        if x > 0:
            rev_str_x = str(x)[::-1] # turn into string then reverse it
            res = int(rev_str_x) # convert back into an int
        else:
            str_x = str(x)
            rev_str_x = str_x[0] + str_x[1:][::-1] # add back the negative sign
            res = int(rev_str_x)

        if res < -2**31 or res > 2**31-1:
            return 0
        
        return res
