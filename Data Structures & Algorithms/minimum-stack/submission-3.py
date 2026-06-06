class MinStack:

    def __init__(self):
        self.support_stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if self.support_stack:
            self.minimum = self.support_stack[-1][1]
        # print(self.support_stack)
        if not self.support_stack: 
            self.minimum = float('inf')
        self.support_stack.append((val, min(val, self.minimum)))

    def pop(self) -> None:
        # print("pop",self.support_stack)
        self.support_stack.pop()

    def top(self) -> int:
        return self.support_stack[-1][0]

    def getMin(self) -> int:
        return self.support_stack[-1][1]


    
