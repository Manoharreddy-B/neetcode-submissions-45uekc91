class MinStack:

    def __init__(self):
        self.support_stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        # if self.support_stack:
        #     self.minimum = self.support_stack[-1][1]
        # if not self.support_stack: 
        #     self.minimum = float('inf')
        if not self.support_stack:
            current_min = val
        else:
            previous_min = self.support_stack[-1][1]
            current_min = min(val, previous_min)
        self.support_stack.append((val, current_min))

    def pop(self) -> None:
        self.support_stack.pop()

    def top(self) -> int:
        return self.support_stack[-1][0]

    def getMin(self) -> int:
        return self.support_stack[-1][1]


    
