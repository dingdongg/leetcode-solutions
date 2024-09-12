# 17 - Letter Combinations of a Phone Number

## General Thoughts
- straightforward backtracking problem

## Things to note
- Simple problem where we need to enumerate all possible cases, given a set of constraints
- DFS + backtracking is good here b/c it allows us to build up a path of combinations
  and recursively build it up until we reach the leaf nodes

### Performance

*Time* - `O(2^n)`, brute force solution where we must traverse all nodes of the decision tree. Each non-leaf node can have 3-4 children

*Memory* - `O(len(digits))`, max length of call stack is equal to the number of digits 

---

## Algorithm
see `main.py`