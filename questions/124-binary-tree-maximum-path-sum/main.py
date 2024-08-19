from typing import Optional, List

"""PATH:
sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them

A node can only appear in the sequence at most once

path does not need to pass through the root

PATH SUM:
sum of the node's values in the path

given the `root` of a binary tree, return the `maximum path sum` of any non-empty path


when computing the sum of the path at node `k`, there are a couple cases to consider:
1. max sum is the value of node `k` and NONE of its chidren sum
2. max sum is the value of node `k` and the sum of its LEFT subtree
3. max sum is the value of node `k` and the sum of its RIGHT subtre
4. max sum is the value of node `k` and the sum of both of its LEFT and RIGHT subtrees
5. max sum is the sum of its LEFT subtree alone
6. max sum is the sum of its RIGHT subtree alone


base cases:
empty node -> 0
leaf node -> node.val + left sum (0) + right sum (0) == node.val

*** a node can only appear in the sequence AT MOST ONCEv (ie. no backtracking)

is the max sum path self-contained within the left/right subtree?
- if so, the current node should not be considered
- but what if by including the current node, the parent node can join it up with another tree
  for a total sum that is substantially bigger than what was originally possible?

  - this means that, at each node, we need to be able to configure whether or not 
    we want to include the current node we're at in the max sum path calculation.
    - otherwise, if we don't want to, 


each node can either be included or not included in the max path sum
- if included, ZERO or ONE of its immediate children can be considered for inclusion as well
    - keep going down like this (0/1) until a children for consideration is rejected
- otherwise, ignore current node but check for other potential max sums in BOTH of its children

if a recursive call returns the max sum of a double path contained within that subtree,


cases:
a. max sum of a double path contained within a recursive subtree + no current node     (DP)
b. max sum of a single path contained within a recursive subtree + current node        (SP)
c. 2 * max sum of single path contained within each recursive subtree + current node   (DP)
d. just the current node (recursive subtrees only bring the sum down; ie. all negative nums)
    - considered as a single path

recursive output: [type, value]
- type is ion range [0, 3] -> denotes the 4 cases above in order
- value is the computed path sum

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.maxpath(root))
    
    def maxpath(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [float('-inf'), float('-inf'), float('-inf'), float('-inf')]

        left_sums = self.maxpath(root.left)
        right_sums = self.maxpath(root.right)

        # type A: double path within a subtree; O(1)
        type_a = max(left_sums[0], right_sums[0], left_sums[1], right_sums[1])

        # type B: single path + current node; O(1)
        type_b = max(
            left_sums[1] + root.val,
            right_sums[1] + root.val,
            root.val,
        )

        # type C: double path that includes the current node; O(1)
        type_c = max(
            left_sums[2],
            right_sums[2],
            root.val,
            left_sums[1] + right_sums[1] + root.val, # form from joining two SPs together
        )

        # it looks like type D isn't needed, since it is already included in type B/C
        # type_d = root.val
        return [type_a, type_b, type_c]
