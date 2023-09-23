from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target_sum = targetSum
        return self.solve(root, 0)

    def solve(self, root: Optional[TreeNode], curr_sum: int) -> bool:
        if root:
            new_sum = curr_sum + root.val
            if root.left or root.right:
                left_has_sum = self.solve(root.left, new_sum)
                right_has_sum = self.solve(root.right, new_sum)
                return left_has_sum or right_has_sum
            return new_sum == self.target_sum
        return False


s = Solution()

root = TreeNode(
    5,
    TreeNode(
        4,
        TreeNode(
            11,
            TreeNode(7),
            TreeNode(2),
        ),
    ),
    TreeNode(
        8,
        TreeNode(13),
        TreeNode(
            4,
            None,
            TreeNode(1),
        ),
    ),
)

root = TreeNode(1, TreeNode(2), TreeNode(3))

print(s.hasPathSum(root, 5))