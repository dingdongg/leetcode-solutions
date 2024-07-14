# 739 - Daily Temperatures

## General Thoughts
- easy

## Things to note
- we're only interested in a *future* day that is warmer
- so it's fine to discard days in the past even if they're warmer than the current day
- with a monotonic stack, we can figure out when we have found the closest warmer day
    - whenever we reach a temperature that is warmer than the temp on top of the stack, 
      we can calculate the closest warmer day for all temps in the stack that are less 
      than the reached temperature

### Performance

*Time* - `O(n)`; we only push items onto a stack once, and maybe one additional pop

*Memory* - `O(n)`; stack and return value array

---

## Algorithm
```
1. init a zeroed array of length len(temperatures)
2. init an empty stack
3. for i in range(len(temperatures)),
    1. while len(stack) > 0 and stack[-1][1] < temperatures[i],
        1. set colder_day = stack.pop()
        2. set res[colder_day[0]] = i - colder_day[0]
    2. stack.push([i, t])
4. return res
```

## Things I learned
- whenever themes like "the next greatest/smallest" comes up, monotonic stack is pretty useful
- in this case the events where the next temperature was *greater* than the top of the stacks signalled us to calculate the index differences

## Things to improve
- still not fully comfortable utilizing stacks