class MinStack:

    def __init__(self):
        self.min_stack = [] # keep track of all the min values
        self.stack = [] # stack that holds the elements

    def push(self, val: int) -> None:
        self.stack.append(val) 

        # check if the val added to stack is a min value
        if self.min_stack == [] or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:  # non-empty list
            popped = self.stack.pop()
            if popped == self.min_stack[-1]: # update min if val removed is min
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack == None: return None  # empty list has no top element
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# all of the functions have a time complexity of O(1)
# space complexity: O(n), the stacks to hold elements and min values
