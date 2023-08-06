from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:   
        slow, fast = head, head

        # while fast is not None and slow is not None:
        #     slow = slow.next
        #     fast = fast.next
        #     if fast != None: fast = fast.next
        #     if fast != None and slow == fast: return True
        # return False

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True
        return False
    

