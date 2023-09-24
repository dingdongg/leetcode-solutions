from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum_so_far = 0

        self.solve(root, 0)
        return self.sum_so_far
    
    def solve(self, root: Optional[TreeNode], prod: int):
        if root:
            new_prod = prod * 10
            new_prod += root.val
            if root.left or root.right:
                self.solve(root.left, new_prod)
                self.solve(root.right, new_prod)
            else:
                self.sum_so_far += new_prod

s = Solution()

root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3),
)

root = TreeNode(
    4,
    TreeNode(
        9,
        TreeNode(5),
        TreeNode(1),
    ),
    TreeNode(0),
)

print(s.sumNumbers(root))
            