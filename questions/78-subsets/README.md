# 78 - Subsets

## General Thoughts
- too easy for a medium, i think this is closer to an easy problem

## Things to note
- learn the concept of power set in stat 302
- given a collection of items, each item `i` can either *be included* in a set, or *not be included* in a set
- by simple permutation, this will yield a total of `2^n` possible sets, given `n` items
- the above can be represented as a binary decision tree
    - at the root, you start off with no items included
    - then, for each level `i`, you recursively compute the possible sets by either including/excluding item `i`
- the above can be done via depth-first search. In DFS, stacks are utilized to "backtrack" to the previous state/parent node

### Performance

*Time* - `O(2^n)` - for `0 <= i < n`, level `i` of the decision tree will yield `2^i` nodes. We visit all these nodes once, which comes to a total of `2^(n+1) - 1` nodes total

*Memory* - `O(log(n))` - maximum size of call stack is determined by the height of our decision tree

---

## Algorithm
```
1. init an empty list (ret)
2. define dfs(stack, level):
    1. if i == length of nums, create a list of current stack contents, push to ret and return
    2. push nums[i] to stack
    3. dfs(stack, i + 1)
    4. pop nums[i] from stack
    5. dfs(stack, i + 1)
3. dfs([], 0)
4. return ret
```
