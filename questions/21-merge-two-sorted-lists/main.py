from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1
        
        curr = ret = list2 if list2.val <= list1.val else list1
        other_next = list2 if list2.val > list1.val else list1

        while curr:
            jump = curr.next
            if jump:
                if jump.val > other_next.val:
                    curr.next = other_next
                    other_next = jump
                curr = curr.next
            else:
                curr.next = other_next
                break
        
        return ret

                

        