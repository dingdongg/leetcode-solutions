from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.stack = []
        self.target_sum = targetSum
        self.ret = []

        self.solve(root, 0)
        return self.ret
    
    def solve(self, root: Optional[TreeNode], curr_sum: int) -> None:
        if root:
            self.stack.append(root.val)
            new_sum = curr_sum + root.val
            if root.left or root.right:
                self.solve(root.left, new_sum)
                self.solve(root.right, new_sum)
            else:
                if new_sum == self.target_sum: self.ret.append(list(self.stack))
            self.stack.pop()
        
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
            TreeNode(5),
            TreeNode(1),
        ),
    )
)

root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(1, TreeNode(2))

targetSum = 0

print(s.pathSum(root, targetSum))