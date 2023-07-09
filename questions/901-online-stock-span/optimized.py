class StockSpanner:
    def __init__(self):
        self.prices = [] # store (price, span on that day)
        # (big -> small from bottom to top of stack)

    def next(self, price: int) -> int:
        """
        main thing to note is that, for all of the prices that are within a span, I can pop 
        them all and encapsulate the span info as a tuple in the form (price, span).
        This gets rid of the need to traverse the span again and again in the future
        """
        span = 1

        while self.prices and price >= self.prices[-1][0]:
            span += self.prices.pop()[1]
        self.prices.append((price, span))
        
        return span
            
        
spans = []
val = [100, 80, 60, 70, 60, 75, 85, 300]

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for v in val:
    spans.append(obj.next(v))

print(spans)