# 235 - Lowest Common Ancestor of a Binary Search Tree

## General Thoughts
- Pretty straightforward. I like my solution, but neetcode's solution is also simple and clever

## Things to note
- If you consider the DFS traversals to nodes `p` and `q`, each from the root of the tree, the LCA is going to be the latest node that has been visited in both traversals.
- Given the constraints of the problem, such a node will always exist (at LEAST the root node)
- if we record the nodes we see as we traverse, and update our LCA node every time we come across a node we've seen, we can return this value at the very end to get our result

### Performance

*Time* - `O(log n)`; usually, trees have a height of `log(n)` and we require 2 DFS traversals 

*Memory* - `O(log n)`; need to keep track of visited nodes in a set. DFS visits `O(log n)` nodes

---

## Optimization notes
- Alternatively, LCA node can be thought of as the node where nodes `p` and `q` end up on different subtrees
- OR, the current node is equal to either `p` or `q`, in which case the current node would be the LCA (there are no lower nodes that will be the ancestor to both `p` and `q`)

### Performance

*Time* - `O(log n)`, 1 DFS traversal

*Memory* - `O(1)`, no need to keep track of visited nodes

---

## Algorithm
- see `optimized.py`

## Things I learned
- observation method is OP!
- write everything down. see problem `#981` notes
