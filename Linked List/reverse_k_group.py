from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # helper fn to reverse k nodes
        # @returns the head and the tail of the reversed group
        def reverseKNodes(head:Optional[ListNode], k: int) -> Optional[ListNode]:
            prev, curr = head, head.next
            
            for _ in range(k - 1):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            head.next = curr
        
            return prev, head
        # end helper fn

        head, tail_1 = reverseKNodes(head, k)

        while tail_1.next:
            curr = tail_1
            for _ in range(k):
                if not curr.next:
                    return head;
                curr = curr.next;

            head_2, tail_2 = reverseKNodes(tail_1.next, k)
            tail_1.next = head_2
            tail_1 = tail_2

        return head