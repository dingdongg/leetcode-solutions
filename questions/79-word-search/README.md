# 79 - Word Search

## General Thoughts
- very straightforward but i struggled :(

## Things to note
- backtracking problem, need to brute force (and this is feasible since the input problem size is relatively small)
- main constraint is that we cannot re-use a cell more than once, so if we encounter a cell we saw before we must terminate
    - this required the use of a set to keep track of the current path in backtracking

### Performance

*Time* - `O(n * m * 4^(word))`; must brute-force every cell in the matrix, with up to 4 recursive calls at every node

*Memory* - `O(word)`; call stack is proportional to the length of the word

---

## Algorithm
see `main.py` :D

## Things to improve
- need to make sure I really spend time on analyzing the problem on paper, without prematurely devising an algorithm