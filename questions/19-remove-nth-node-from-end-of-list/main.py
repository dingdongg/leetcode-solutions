from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the length of the linked list,
        # then do a second traversal from the head to find the corresponding node and delete it

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        target = length - n

        # if index is 0, the  loop never executes
        # simply increment head pointer and return it
        if target == 0: return head.next

        prev = None
        curr = head
        for _ in range(target):
            prev = curr
            curr = curr.next
        
        # curr will be the node to delete. re-arrange pointers
        if curr == None: prev.next = None
        else: prev.next = curr.next

        return head
    
ex1 = ListNode(1, ListNode(2))

vals = [1, 2, 3, 4, 5]
listVals = list(map(lambda v: ListNode(v), vals))

for i in range(1, len(listVals)):a
    listVals[i-1].next = listVals[i]

before = listVals[0]

while before:
    print("before val: ", before.val)
    before = before.next

prunedLL = Solution().removeNthFromEnd(listVals[0], 1)

while prunedLL:
    print("val: ", prunedLL.val)
    prunedLL = prunedLL.next

