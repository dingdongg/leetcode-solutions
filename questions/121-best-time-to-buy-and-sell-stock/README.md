# 121 - Best Time to Buy and Sell Stock

## General Thoughts
- easy

## Things to note
- good intro to sliding windows/two-pointer technique
- whenever we see a lower price point, it makes more sense to buy at that lower price than to sell
- the problem with the brute-force solution is that, regardless of the whether or not the transaction would yield a negative profit (ie. sell < buy), it enumerates all further solutions
    - with the sliding window technique, it discards these options since it's more worth to look at possible profits when we execute a buy at the lower price point

### Performance

*Time* - `O(n)` - iterate two pointers through the array linearly

*Memory* - `O(1)`

---

## Algorithm
```
1. if there are less than 2 prices in the array, return 0
2. set l, r = 0, 1
3. set profit = 0
4. while r < length of the array,
    1. set buy, sell = prices[l], prices[r]
    2. if buy > sell, set l = r (essentially buying at the lower price now)
    3. else, set profit = max(profit, sell - buy)
    4. increment r by 1
5. return profit
```

## Things I learned
- 

## Things to improve
- gotta get more comfortable with sliding windows