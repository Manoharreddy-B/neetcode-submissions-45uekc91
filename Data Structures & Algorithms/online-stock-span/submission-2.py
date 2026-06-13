class StockSpanner:

    def __init__(self):
        self.stack = []
        self.length = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price :
            self.stack.pop()[1]
        if not self.stack:
            answer = self.length + 1
        else:
            answer = self.length - self.stack[-1][1] 
        self.stack.append((price,self.length))
        self.length += 1
        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)