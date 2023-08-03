# 75 - Sort Colors

## General Thoughts
- Pretty straightforward. Got destroyed by the previous problem so this was a nice change of pace 🥲

## Things to note
- There are only a fixed set of unique numbers in the array (0, 1, and 2). This means a brute force solution would be `O(n)`

### Performance

*Time* - `O(n)`

*Memory* - `O(1)` - even if you decide to allocate an array to keep track of the color count, there will be at most 3 entries in the array so the size always fixed

---

## Optimization notes
- Apparently there is an algorithm called the *Dutch National Flag Algorithm*, which is a variation on the 3-way partitioning method. It's a legitimate one pass algorithm in that we only need one loop through the array (as opposed to 2/3 in my solution)

### Performance

*Time* - `O(n)`, since you still have one loop through the array

*Memory* - `O(1)`, just need some pointers (left, mid, right)

---

## Algorithm
```
1. Initialize a starting index variable
2. for every color possible (0, 1, 2),
    1. for i in range 0..n,
        1. if nums[i] == color,
            1. swap nums[start] and nums[i]
            2. increment start by 1
```
## Things I learned
- Nothing much here, didn't even seem like a two-pointer question at first

## Things to improve
- ***CONSISTENCY IS KEY***
    - I have to stay on top of things (ie. a few leetcodes every day) if I don't want to be rusty which will only end in frustration