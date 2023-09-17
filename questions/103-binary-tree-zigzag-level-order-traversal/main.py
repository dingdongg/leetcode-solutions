from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Queue:
    def __init__(self) -> None:
        self.back = []
        self.front = []
    
    def enqueue(self, val: any) -> None:
        self.back.append(val)
    
    def dequeue(self) -> any:
        if not self.front:
            while self.back: 
                self.front.append(self.back.pop())
        return self.front.pop()

    def empty(self) -> bool:
        return len(self.back) + len(self.front) == 0
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queue = Queue()
        if root: self.queue.enqueue([root])
        switch_order = True
        ret = []

        while not self.queue.empty():
            curr_level = self.queue.dequeue()
            ret.append([n.val for n in curr_level])
            next_level = []
            
            while curr_level:
                node = curr_level.pop()
                if switch_order:
                    if node.right: next_level.append(node.right)
                    if node.left: next_level.append(node.left)
                else:
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
                    
            if next_level: self.queue.enqueue(next_level)
            switch_order = not switch_order

        return ret


s = Solution()
# root = TreeNode(
#     3,
#     TreeNode(9),
#     TreeNode(
#         20,
#         TreeNode(15),
#         TreeNode(7),
#     ),
# )

root = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(4),
        None,
    ),
    TreeNode(
        3,
        None,
        TreeNode(5),
    ),
)
print(s.zigzagLevelOrder(root))