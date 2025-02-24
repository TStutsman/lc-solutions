from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tens = 0
        dummy = ListNode()
        cur = dummy

        n, m = l1, l2
        while n or m:
            a = n.val if n else 0
            b = m.val if m else 0
            c = a + b + tens

            tens = c // 10
            cur.next = ListNode(c % 10)

            n = n.next if n else None
            m = m.next if m else None
            cur = cur.next
        
        if tens:
            cur.next = ListNode(tens)

        return dummy.next