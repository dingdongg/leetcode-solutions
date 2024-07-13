from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2nd solution: do it all in one pass
        # the problem is that 1 traversal is necessary to calculate deletion index
        # if we store each node in an array, we achieve O(1) access time!
        if head.next == None: return None

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        
        target = len(nodes) - n
        
        if target == 0:
            # return index 1
            return nodes[1]
        
        # otherwise, re-arrange pointers and return index 0
        target_node = nodes[target]
        nodes[target - 1].next = target_node.next
        return nodes[0]

