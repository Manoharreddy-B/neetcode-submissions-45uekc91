class StockSpanner:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.answer = 1

    def next(self, price: int) -> int:
        index = 0
        while self.stack and self.stack[-1][0] <= price :
            index = self.stack.pop()[1]
        if not self.stack:
            self.answer = self.length + 1
        else:
            self.answer = self.length - self.stack[-1][1] 
        self.stack.append((price,self.length))
        self.length += 1
        return self.answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)