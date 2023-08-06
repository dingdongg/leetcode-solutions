from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     ptr = head
    #     nodes = set()

    #     while ptr != None:
    #         if ptr in nodes: return ptr
    #         nodes.add(ptr)
    #         ptr = ptr.next
    #     return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        loop_exists = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                loop_exists = True
                break
        
        if not loop_exists: return None

        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow