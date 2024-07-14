# 155 - Min Stack

## General Thoughts
- hard
- ended up overthikning the problem again

## Things to note
- every incoming value to our stack is either the new minimum or not.
- thus, with every insert, we can keep track of a history of min values over time using a monotonically decreasing stack

### Performance

*Time* - `O(1)` for all methods, including `getMin()`

*Memory* - `O(n)`

---

## Algorithm
```
1. MinStack()
    1. set data = [], mins = []
2. push(val)
    1. data.push(val)
    2. if len(mins) == 0, mins.push(val)
    3. else, push the minimum of mins[-1] and val into mins
3. pop()
    1. data.pop()
    2. mins.pop()
4. top()
    1. return data[-1]
5. getMin()
    1. return mins[-1]
```
## Things I learned
- monotonic stack use cases are still tricky, but drawing the problem out makes it easy to spot their uses

## Things to improve
- When the problem is becoming way too hard, try to go back to a blank canvas and draw out an example
- in this instance, going back and drawing out a mapping of the `push()` values and the min state after each `push()` call helped me realize that a monotonic stack can be used to kee ptrack of the minimum