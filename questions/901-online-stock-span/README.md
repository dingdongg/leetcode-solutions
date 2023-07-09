# 901 - Online Stock Span

## General Thoughts
- Easy. Starting from the brute force solution and optimizing from there on out helped
me see the duplicated work and how I could optimize it to improve performance

## Things to note
- Because the span must be *consecutive* (back-to-back), you stop incrementing the span count
once you hit a higher price
- If you store the span along with the price, there is no need to store the smaller elements that are included in the span
- brute force solution doesn't take advantage of the above, resulting in higher runtimes
- on a sufficiently random set of prices, the brute force can be trivially optimized by skipping pointers equal to the span size of any given day. However, this still yields `O(n^2)` worst case runtime

### Brute Force Performance

*Time* - `O(n^2)` - with each price (of which there are `n`), you are doing `O(n)` traversals

*Memory* - `O(n)` - proportional to the number of function calls

---

## Algorithm
```
1. While pointer i is not below 0,
    1. if today's price is higher than the price at day i,
        1. increase the span by the span at day i
        2. decrease i by the span at day i
    2. otherwise, exit loop
2. push (today's price, today's span) to the back of the list
3. return today's span
```
---

## Optimization notes
- In the brute force version, you store all `n` prices in a list, so you must do an `O(n)` traversal for every price, leading to `O(n^2)` runtime
- because span consists of LTE prices back-to-back, I can skip redundant span calculations by popping the prices in the span, and storing this span along with the price in a stack
- stack is useful because we can maintain a chronological order of the prices (which matters for this problem) 
- whenever I have a price with `span > k`, I can pop `k` elements from the stack
    - then I can push `(price, k + 1)` to the stack to skip redundant span calculations

### Performance

*Time* - `O(n)` - there is at most 1 `pop()` and 1 `push()` executed per item, both of which are `O(1)` operations

*Memory* - `O(n)` - on average there should be less items than the brute force since we're popping, but worse case is still the same (ie. prices decrease every day)

---

## Optimized algorithm
```
1. while the stack isn't empty and today's price >= price at the top of the stack:
    1. pop stack
    2. increment span by the span of the item popped 
2. push `(price, span)` to the stack
3. return span
```
## Things I learned
- If stuck, resort to brute force solution and then optimize!
    - From the brute force solution, identify parts that are redundant and can be optimized based on some fact deduced from the problem
- Thinking "problem-first" instead of "DS/technique-first" always helps