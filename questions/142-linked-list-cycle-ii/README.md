# 142 - Linked List Cycle II

## General Thoughts
- Pretty straightforward once I saw the solution, although I was very close to solving the problem on my own.

## Things to note
- The naive approach is to keep track of the nodes we have seen thus far, and once we come across an already seen node, we return that node
- can use a set for this

### Performance

*Time* - `O(n)`

*Memory* - `O(n)` to keep track of nodes seen

---

## Optimization notes
- To reduce memory usage down to `O(1)`, there are a few things we must observe:
    - For a linked list with `n` nodes and a cycle of size `k`, the tortoise-hare method will converge at the node in the cycle that is `n % k` steps away from the start of the cycle.
    - ex) `n = 11, k = 4`: the cycle will be detected at the node that is `11 % 4 = 3` steps away from the cycle start
        - More generally, it takes `(n % k) + xk` steps to reach the cycle start node, where `x` is any positive integer
        - the number of nodes stepped to reach the cycle start node will be equal to one of the values specified by the equation `(n % k) + xk`, as does the node at which the algorithm converged
        - so, once we converge we can set a pointer back to the head and move them by 1 until they meet at the cycle start!

### Performance

*Time* - `O(n)`, need to see neetcode's explanation on this

*Memory* - `O(1)`, only additional pointers used

---

## Algorithm
```
1. Initialize the slow and fast pointers to the head of the linked list
2. Set a variable loop_exists to false
3. While fast is non-null and fast.next is non-null,
    1. Move slow pointer by 1
    2. Move fast pointer by 2
    3. if slow == fast, set loop_exists to true and break the loop
4. if loop_exists is false, return null
5. reset fast's value to head
6. while fast != slow,
    1. move slow pointer by 1
    2. move fast pointer by 1
7. return fast (or slow)
```
## Things I learned
- I did pretty good analyzing the problem and figuring out some mathematical facts about the problem 

## Things to improve
- I was literally one step away from the solution (didn't notice that the distance from head to the start of the cycle is equal to the distance from the converging node to the start of the cycle)
    - tbf I was falling asleep towards the end, so maybe I just need to sharpen my focus for next time