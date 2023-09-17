from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        self.bottomUp(root, 0)
        self.levels.reverse()
        return self.levels
    
    def bottomUp(self, root: Optional[TreeNode], level: int):
        if root:
            if level == len(self.levels): self.levels.append([])
            self.bottomUp(root.left, level + 1)
            self.bottomUp(root.right, level + 1)
            self.levels[level].append(root.val)

