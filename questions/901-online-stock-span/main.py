class StockSpanner:
    def __init__(self):
        self.prices = [] # store (price, span on that day)

    def next(self, price: int) -> int:
        span = 1
        i = len(self.prices) - 1
        while i > -1:
            spannable = price >= self.prices[i][0]
            if spannable: 
                span += self.prices[i][1]
                i -= self.prices[i][1]
            else: break
        self.prices.append((price, span))
        
        return span
            
        
spans = []
val = [100, 80, 60, 70, 60, 75, 85, 300]

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for v in val:
    spans.append(obj.next(v))

print(spans)