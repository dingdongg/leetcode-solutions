# 1996 - The Number of Weak Characters in the Game

## General Thoughts
- Pretty difficult to find out that sorting had to be used. Once that was figured out, 
the rest of the solution was easy to understand
- Because the problem was listed under "monotonic stack", I was fixated on using a monotonic
stack again, which was why I struggled so much

## Things to note
- for any 2 characters `i` and `j` where `i != j`, `i` is weaker than `j` if `i.attack < j.attack` AND `i.defense < j.defense`
- once we sort the array in order of **descending attack** and **ascending defense**, we only need to compare the **defenses of each player vs. the maximum defense** seen so far, because as we iterate through the list from left to right, the attack is in non-increasing order
- once we see that `p[1] < maxDefense`, at this point we know that `p`'s attack is strictly lower, so we can increment the count of weak characters. This is because, if `p`'s attack was not strictly lower, `p` should have come earlier in the list (the list is in descending order of attack)

### Performance

*Time* - `O(n log n)` because we have to sort the list

*Memory* - `O(1)` excluding the input list

---

## Algorithm
```
1. Sort the input list in descending attack order and ascending defense order
2. Initialize variables to keep track of count and max defense seen so far
3. For each player in the sorted input list,
    1. if `player[1] < maxDefense`, increment count
    2. else, `maxDefense = player[1]`
4. return `maxDefense`
```
## Things I learned
- Got stuck on using the DS under which this question was listed. 
- I need to work on really analyzing the problem without getting DS/techinques involved prematurely