from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, fast = None, head, head

        count = 0
        while count < n:
            fast = fast.next
            count += 1

        while fast:
            prev = curr
            curr = curr.next
            fast = fast.next
        
        if not prev:
            return head.next
        
        prev.next = curr.next
        return head