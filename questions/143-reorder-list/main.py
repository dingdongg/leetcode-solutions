from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next: return
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        jump = None
        while slow:
            jump = slow.next
            slow.next = prev
            prev = slow
            slow = jump
            
        next_head = prev
        _head = head
        while _head != jump:
            jump = _head.next
            _head.next = next_head
            _head = next_head
            next_head = jump
        
