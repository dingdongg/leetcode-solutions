from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_so_far = { 'res': -1 }
        self.maxDepth(root, max_so_far)
        return max_so_far['res']
        
    def maxDepth(self, root: Optional[TreeNode], maxSoFar: dict) -> int:
        if not root: return 0

        left_depth = self.maxDepth(root.left, maxSoFar)
        right_depth = self.maxDepth(root.right, maxSoFar)

        if left_depth + right_depth > maxSoFar['res']:
            maxSoFar['res'] = left_depth + right_depth

        return 1 + max(left_depth, right_depth)
        

root = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(4),
        TreeNode(5),
    ),
    TreeNode(3),
)

s = Solution()
print(s.diameterOfBinaryTree(root))