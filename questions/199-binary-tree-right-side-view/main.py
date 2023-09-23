from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightmost_nodes = []

        self.solve(root, 0)
        return self.rightmost_nodes

    def solve(self, root: Optional[TreeNode], height: int) -> None:
        if root:
            if height == len(self.rightmost_nodes): self.rightmost_nodes.append(root.val)
            self.solve(root.right, height + 1)
            self.solve(root.left, height + 1)

s = Solution()
root = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(5),
        None, 
    ),
    TreeNode(3),
)
print(s.rightSideView(root))