class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


"""
The plan of this was to use a stack to keep track of the elements. For each push, we add the element to the stack. For pop, we remove the top element. For top, we return the top element. For getMin, we iterate through the stack to find the minimum element and return it. We also use a temporary stack to restore the original stack after finding the minimum.
"""
