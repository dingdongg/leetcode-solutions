from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        left_depth = self.minDepth(root.left) or float("infinity")
        right_depth = self.minDepth(root.right) or float("infinity")
        return 1 + min(left_depth, right_depth)
    

s = Solution()
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7),
    ),
)
print(s.minDepth(root))