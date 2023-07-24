# 977 - Squares of a Sorted Array

## General Thoughts
- Straightforward. There was a trick that you had to notice in order to solve the problem but it wasn't too hard to notice it

## Things to note
- There are 2 main cases:
    1. the rightmost integer is `> 0`
        - in this case, the maximas in the squared array appear at either ends of the array, so we can start reading the maxes to get a *non-increasing* list
        - then you can reverse this list in `O(n)` time and return it
    2. the rightmost integer is `<= 0`
        - in this case, the maxima will be at the left of the array after squaring
        - start squaring from the right end of the array and return the list

### Performance

*Time* - `O(n)`, this is a two-pointer method with constant number of `O(1)` operations done on each item of the list

*Memory* - `O(n)`, needed to hold the intermediate non-increasing collection of items

---

## Optimization notes
- will have to come back to this problem and see if there is a way to optimize further

### Performance

*Time* - ``

*Memory* - ``

---

## Algorithm
```
1. Initialize left and right pointers to be at either ends of nums
2. Initialize an empty return array (ret)
3. if nums[r] > 0,
    1. Initialize another array sorted_nums
    2. while l <= r,
        1. compare the squares of nums[l] and nums[r] and append the max to sorted_nums
        2. if nums[l] >= nums[r] or l == r, increment l by 1
        3. otherwise, increment r by 1
    3. start from the back of sorted_nums and append the square of each item to ret
4. otherwise, start from the back of nums and append the square of each item to ret
5. return ret
```
## Things I learned
- The hardest part of this problem was noticing the pattern in the array (local maximas appear at the end(s) of the array), I picked up on it without much trouble

## Things to improve
- Not sure but I think my logical thinking improved; Noticing that sorting is `O(n log n)`, I looked for alternative solutions to bring the runtime down to `O(n)` (hence the use of two-pointer technique)