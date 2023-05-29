class Solution:
    def isValid(self, s: str) -> bool:

        # we can use a stack
        stack = []
        # the pairings for each type of parentheses
        p = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in range(len(s)):
            # check if opening parenethese or closing
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i]) # push to top of stack
            else:
                # if closing and the top of stack is not the 
                # matching pairing or stack is already popped empty
                # and we have another closing then it's not valid
                if len(stack) == 0 or stack.pop() != p[s[i]]:
                    return False

        # return if the stack if empty i.e. no mismatches
        return len(stack) == 0
