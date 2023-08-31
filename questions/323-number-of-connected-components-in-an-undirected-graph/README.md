# 323 - Number of Connected Components in an Undirected Graph

## General Thoughts
- Pretty straightforward after I learned about disjoint sets and its operations? 
- Application of disjoint set is pretty braindead too, seems more like an LC easy

## Things to note
- as you iterate through the list of edges, you can keep track of the connected state of nodes via disjoint sets
- with every edge `[x, y]`, you can perform a union between the disjoint sets that hold `x` and `y`
    - except when `x` and `y` belong to the same set; then just skip the edge
- every time there is a successful union between two sets, the number of connected components decreases by 1 (2 sets merge into 1)
- number of possible connected components is in the range `[1, n]`
    - the graph could be fully connected, or every node might be detached on its own

## Optimization notes
- the only optimization possible here is with the disjoint set operations themselves
1. for **disjoint set `find()`**, you want to use path compression to "compress" the heights of the underlying tree implementation of the sets 
    - this ensures `O(log n)`???? (check this again) runtime, as opposed to the `O(n)` worst case for unoptimized find operations
    - once you find the rep of a set, we point the initial node we queried with directly to that rep
2. for **disjoint set `union()`**, you should merge based on a heuristic:
    - union by rank: this compares the heights of the two sets. If `rank(A) < rank(B)`, merge A under B and viceversa
        - if ranks are equal, doesn't matter; just make sure to increment the rank of the higher set by 1
    - union by size: same principle, but uses the total number of elements in the set

### Performance

*Time* - `O(α(n))` - `α` is the inverse Ackermann function; Wikipedia states that `α(n) < 5` for any practical input, so time complexity is basically **constant**

*Memory* - `O(n)` - `parents` and `ranks` array are of size `n`

---

## Algorithm
```
1. Initialize a parents array [0 1 2 .. n-1]
2. Initialize a ranks array of all 0s of length n
3. Set number of components to n
4. For every edge in edges,
    1. perform a union on elements edge[0] and edge[1] as follows:
        1. find the leader of edge[0]
        2. find the leader of edge[1]
        3. if leaders from first_leader (4.1.1.) and second_leader (4.2.2.) are equal, return
        4. get the ranks of first_leader and second_leader
        5. if rank(first_leader) < rank(second_leader), set parents[first_leader] to second_leader
        6. if rank(first_leader) > rank(second_leader), set parents[second_leader] to first_leader
        7. if ranks are equal, set either leader's parent to the other, and increment rank of higher set
    2. if union was successful, decrement components by 1
5. return components
```
## Things I learned
- Disjoint sets seemed pretty scary, but I learned that it's a pretty useful data structure with interesting runtime complexities (inverse ackermann??)

## Things to improve
- none here, just keep practicing graph problems!