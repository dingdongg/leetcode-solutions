# 150 - Evaluate Reverse Polish Notation

## General Thoughts
- easy

## Things to note
- with RPN you work from left to right (since the ordering is `number number operator`)
- this means that, when you add the numbers to a stack, there will always be enough
numbers to support each operator
- by using a stack, the "innermost" operations are executed first naturally (due to LIFO nature of stacks), so there is no need for explicit parentheses to do order of operations

### Performance

*Time* - `O(n)`

*Memory* - `O(n)`

---

## Algorithm
```
1. set up an empty stack (operands)
2. for each token in tokens,
    1. if t is a number, push to the operands stack
    2. otherwise, 
        1. set second = operands.pop()
        2. set first = operands.pop()
        3. if token is "+", push (first + second) to stack
        4. if token is "-", push (first - second) to stack
        5. if token is "*", push (first * second) to stack
        6. if token is "/", push (first / second) to stack (after truncating towards zero)
3. return operands[0]
```

## Things I learned
- nothing substantial

## Things to improve
- tbh I only solved this problem this easily because of the wiki link they posted on LC