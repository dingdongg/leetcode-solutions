# 202 - Happy Number

## General Thoughts
- Easy application of the tortoise-hare algo

## Things to note
- Naive approach is to use a set to keep track of the numbers seen so far
    - If we compute a value that is in this set, we know we have "looped back" so we can return `False`
    - If we compute the value to be 1, then this is a happy number (return `True`)

### Performance

*Time* - `` this would correspond to the number of integers included in this loop

*Memory* - `` this would correspond to the number of integers included in this loop

---

## Optimization notes
- If we want to use constant memory, we can use the tortoise-hare method and modify it to our use case
- for `n = 2`, the sequence is as follows: `2, 4, 16, 37, 58, 89, 145, 42, 20, 4, ...`
    - notice that the sequence **loops back** to `4`
- we can think of this sequence as the sequence of nodes traversed in a linked list with a cycle
    - thus, we can use the tortoise-hare method to detect a cycle
        - if a cycle is detected, return `False`
        - if a number boils down to 1, return `True`

### Performance

*Time* - `` ??? this would correspond to the number of integers included in this loop

*Memory* - `O(1)`, just 2 pointers required and call stacks for the `sum_digits_squared()` method calls

---

## Algorithm
```
1. Initialize slow and fast pointers to n
2. In an infinite loop,
    1. set slow pointer to be one iteration of sum_digits_squared()
    2. set fast pointer to be two iterations of sum_digits_squared()
    3. if slow == 1, return True
    4. if slow == fast, return False 
```
## Things I learned
- This was a neat variation on the tortoise-hare problem, but it would have been difficult to notice without walking through an example til the end. **ALWAYS WORK THROUGH EASY EXAMPLES!**
