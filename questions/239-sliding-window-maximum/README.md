# 239 - Sliding Window Maximum

## General Thoughts
Very hard, couldn't solve on my own without checking the solution. My biggest mistake was being 
fixated on the "sliding window" part and couldn't think of other ways to solve the problem.

Also, I need to review common data structures like queues and their operation runtimes.

I need to analyze the problem to find logical facts about the problem, find operations that need to be fast, which will guide me to
the appropriate data structure to take advantage of.

## Things to note
- The main thing to notice is that, in any given window, ***the elements to the left of the 
window's maximum is irrelevant***. This is because:
    1. the window is sliding to the right,
    2. which means that, once we find the max of a window, all elements
       to the left of that value can **never** be the max for future windows
    
- So we can discard them. In the following example,
    ```
    [1  1  1  4  1  1] 6; k = 6
    ```
    The three 1s to the left of 4 are *irrelevant*, since, as we slide our window to the right,
    none of them can ever be the maximum.
    - This is what the brute force solution fails to address; after you advance your window by 1 element to the right, why waste time looking through the **entire** window again when you already looked through the first `k-1` elements? This also means that the brute force solution looks at the elements to the left of the max value (which can be discarded), resulting in runtime overhead
    - after you look through `1 1 1 4 1 1` as part of the first window, in the second window you should only need to compare `6` to `4 1 1`

- This is why a **monotonically decreasing deque** is useful.
    1. *monotonicity* allows us to store the max value of a window at the front of the deque,
        and also helps us keep track of the "inner" contents of the window in case we pop a max value
        - this is why the traditional sliding window technique doesn't work here, since 
          we lose information on the "inner" contents of the window
    2. *deque* allows us to store the max values in the current window, and allows us to 
        pop from the front/push from the back to simulate the window moving in `O(1)` time
        - once we find a new max, we can pop from the back of the deque until the back of the deque is no longer smaller than our new max
    

### Performance

*Time* - `O(n)` - for each element, we pop and push them from/to the deque once each (both `O(1)`)

*Memory* - `O(n)` - worst case the window is size `len(nums)`, deque may become size of `nums`

---

## Algorithm
```
1. Initialize left and right pointers to track the length of window
2. Initialize ret list and a deque
3. while the right pointer hasn't gone past the last element,
    1. while deque isn't empty AND the current number is greater than the back of deque:
        1. pop from the back of deque
    2. insert the current number
    3. if our window length (r - l + 1) is k,
        1. append the front of the queue (the max of the window) to ret list
        2. if the front of the queue is an element behind the left pointer, pop it from deque
        3. increment left pointer
    4. increment right pointer
4. return ret list
```
## Things I learned
- Don't start the problem by thinking of which DS/technique to use
- **DO START** by just analyzing the problem and logically deduce facts about it
    - as you gather enough facts, think of DS/techniques that could support your use case
    - ex) in this problem, the key point was that all elements to the left of a max value is useless

        🟠 we still need to keep track of the inner contents and be able to pop them easily, so heap would be costly and not good; sliding window technique wouldn't be useful as we lose info on the inner contents

        🟠 since the window slides to the right, we need to be able to "pop" from the left side of our window and "push" into the right side of the window, which means a queue would be nice

        🟠 to always have the maximum value of the window easily accessible, we can make this a monotonically decreasing queue (which means we need to be able to pop from *both* sides of the queue, so a deque is now more appropriate)
- Don't get hung up on one technique/data structure. If something really isn't working out, approach the problem from a different perspective
- Even if it's tempting to just start coding the solution, **do not do this** until you have a solid algorithm on paper with the proper DS/techniques (and reasoning) to back it up