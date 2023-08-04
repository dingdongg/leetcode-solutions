# 713 - Subarray Product Less Than K

## General Thoughts
- Really hard. Had to put this one off on my first attempt to come back to it with a fresh perspective. how is this a medium???

## Things to note
- As you encounter more and more items in the array, the *maximum* number of new subarrays that you can add is bounded by the **length of the subarray** at that point. For instance,

```
    [10   05   02   06]
     ^^                 add 10 to seen list, # new subarrays is 1 (just the [10])

    [10   05   02   06]
     ^     ^            add 5  to seen list, # new subarrays is 2 ([5] and  [10 5])

    [10   05   02   06]
     ^          ^       subarray is now > k, shrink before counting (if we increment by the # subarrays now, we would erroneously count [10 5 2]; we need to see how many invalid subarrays to filter out)
    
    [10   05   02   06]
          ^     ^       subarray is now <= k, # new subarrays is 2 ([2] and [5 2])

    [10   05   02   06]
          ^          ^  subarray is still <= k, # new subarrays is 3 ([6], [2 6], and [5 2 6])
```

### Performance

*Time* - `O(n)`, you do one iteration through the array and perform `O(1)` operations on each item

*Memory* - `O(1)`, pointers and extra constant variables

---

## Algorithm
```
1. If k <= 1, return 0
2. Initialize left and right pointers at the left of the array
3. Initialize count as 0 and product as 1
4. While right pointer isn't out of bounds,
    1. multiply prod by nums[right]
    2. While prod >= k,
        1. divide prod by nums[left]
        2. increment left
    3. Increment count by the current size of the window
5. return count
```
## Things I learned
- Can't stress the importance of base cases & a solid dry run enough
- If the solution seems like it's getting too complicated in your head, you are overcomplicating things 90% of the time
- I am pretty good at recognizing sliding window patterns

## Things to improve
- CONSISTENCY
- Just a week of hiatus is enough to make me rusty, need to keep this going daily