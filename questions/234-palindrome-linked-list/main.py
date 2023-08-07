from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     if head.next == None: return True
    #     slow = fast = head
    #     seen = []
    #     length = 1

    #     while fast and fast.next:
    #         seen.append(slow.val)
    #         slow = slow.next
    #         fast = fast.next
    #         length += 1
    #         if fast.next:
    #             fast = fast.next
    #             length += 1

    #     if length % 2 == 1: seen.append(slow.val)

    #     while slow:
    #         if not seen or slow.val != seen.pop(): return False
    #         slow = slow.next
    #     return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None: return True
        if head.next.next == None: return head.val == head.next.val
        slow = fast = head
        length = 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            length += 1
            fast = fast.next
            if fast: length += 1
        
        prev = slow if length % 2 == 1 else None
        jump = None
        if length % 2 == 1: slow = slow.next
        
        while slow:
            jump = slow.next
            slow.next = prev
            prev = slow
            slow = jump
        other_head = prev
        _head = head
        while other_head != None and _head != other_head:
            if other_head.val != _head.val: return False
            other_head = other_head.next
            _head = _head.next
        return True

        
        
