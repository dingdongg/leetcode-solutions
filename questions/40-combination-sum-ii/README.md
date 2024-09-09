# 40 - Combination Sum II

## General Thoughts
- pretty complicated, since it draws on a couple of key insights from previous problems

## Things to note
- the key thing to note is that we have to generate our decison tree carefully, so that we can avoid
the generation of duplicate nodes altogether
    - the naive way still maintains some duplicates, which requires an expensive constant time operation
    for duplicate checks
- see the mechanism for duplicates elimination in `Combination Sum I` and `3 Sum`
    - also see the notes in `main.py` @ line 150

### Performance

*Time* - `O(n * 2^n)` - `O(n)` operation to copy list into the solution set and roughly `O(2^n)` nodes traversed

*Memory* - `O(n)` - the maximum size of the call stack will be proportional to the length of the array

---

## Algorithm
```
1. sort the candidates list
2. init an empty return list ret
3. def solve(seq, i, sum_so_far):
    1. if i == len(candidates), 
        1. if sum_so_far == target, append a copy of seq to ret
        2. return
    2. if sum_so_far < target,
        1. set idx = i
        2. while idx < len(candidates):
            1. append candidates[idx] to seq
            2. call solve(seq, idx + 1, sum_so_far + candidates[idx])
            3. pop from seq
            4. increment idx by 1
            5. while idx < len(candidates) and candidates[idx] == candidates[idx - 1], increment idx by 1
    3. else if sum_so_far == target,
        1. append a copy of seq to ret
4. call solve([], 0, 0)
5. return ret
```
## Things I learned
- for tree problems, it's important to note that the generation of the tree itself can be pivotal in solving the problem
    - in this case, the decision tree had to be generated in a way where we removed all duplicates from consideration
