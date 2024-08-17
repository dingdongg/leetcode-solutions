class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val > root.val and q.val > root.val:
                # both p and q on right subtree
                root = root.right
            elif p.val < root.val and q.val < root.val:
                # both p, q on the left subtree
                root = root.left
            else:
                # captures case where root == p or q, or there is a split
                return root