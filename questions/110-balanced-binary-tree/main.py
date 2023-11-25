from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced 

    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1: self.balanced = False

        return 1 + max(left_h, right_h)
    

s=Solution()
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(
            15,
            TreeNode(36),
            TreeNode(12),
        ),
        TreeNode(7),
    ),
)

print(s.isBalanced(root))