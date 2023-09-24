from typing import List

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    """
    @param root: Root node of a binary tree.
    @param arr: An array of integers.
    @return: If the array is a valid sequence.
    """
    def is_valid_sequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.seq = arr

        return self.solve(root, 0)
    
    def solve(self, root: TreeNode, height: int) -> bool:
        if root:
            if len(self.seq) <= height or root.val != self.seq[height]: return False

            if root.left or root.right:
                left_seq_is_valid = self.solve(root.left, height + 1)
                right_seq_is_valid = self.solve(root.right, height + 1)
                return left_seq_is_valid or right_seq_is_valid
            return root.val == self.seq[height]
        return False
    

s = Solution()

root = TreeNode(
    0,
    TreeNode(
        1,
        TreeNode(
            0,
            None,
            TreeNode(1),
        ),
        TreeNode(
            1,
            TreeNode(0),
            TreeNode(0),
        ),
    ),
    TreeNode(
        0,
        TreeNode(0),
        None,
    ),
)

arr = [0,1,1]

print(s.is_valid_sequence(root, arr))
            