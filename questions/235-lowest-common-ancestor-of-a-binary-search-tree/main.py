from typing import Optional

"""BST (binary search tree)

find the lowest common ancestor (LCA) node of 2 given nodes in the BST

LOWEST COMMON ANCESTOR:
- a node denoted `T`, defined bwetween two nodes `p` and `q`
- where both `p` and `q` are direct/indirect descendants of `T`
- a node can be a descendant of itself
        - isDescendant(A, A) # true
        - see example 2

CONSTRAINTS:
p != q
p, q exist in the BST
all node values are unique

given two nodes p and q, looking for a node T such that T is in range [p, q] (if we assume p < q)
- node T must have both p and q as its descendants

- assume that p < q (but even if p > q, these facts should still hold if we swap variables around)

- at a given node k,

1. p is to the right of k
    - this means that q must also be to the right. recurse on right subtree
2. p is to the left of k
    - check the value of q
        1. if q is also to the left of k, then recurse on left subtree
            - this current node cannot be LCA, as we can go down at least 1 more level
        2. else if q is to the right of k,
            - LCA node must be somewhere in between
3. p is equal to k
    - LCA will be k if q is a descendant of p
    - otherwise, we must look upward to find the LCA node


NEW IDEA: 
1. get the DFS traversal path from root to p (+ a set version)
2. get the DFS traversal path from root to q (+ a set version)
3. walk back on the nodes traversed for p:
    1. if the current node is in the set for nodes seen to q, that is the LCA. return
    - if we wanted to make a small optimization, we can check the lengths of 
    steps 1 and 2 and traverse the shorter one


[6, 2]
[6, 8]


[6, 2, 0] + set

[6, 2, 4, 5] + set"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.seen_nodes = set()
        self.lca: Optional[TreeNode] = None

        self.dfs(root, p)
        self.dfs(root, q)

        return self.lca
        
    def dfs(self, root: Optional[TreeNode], target: TreeNode):
        if root is None: return

        if root not in self.seen_nodes:
            # node never seen, add it to set
            self.seen_nodes.add(root)
        else:
            self.lca = root
        
        if root.val == target.val: return
        elif root.val < target.val: self.dfs(root.right, target)
        elif root.val > target.val: self.dfs(root.left, target)
