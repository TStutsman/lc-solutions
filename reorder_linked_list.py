# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head or not head.next or not head.next.next: return

#         second = head.next
#         third = second.next
#         second.next = third.next
#         third.next = second
#         head.next = third
        
#         curr = second.next

#         while curr:
#             odd = head
#             even = head.next
#             while even and even.next:
#                 # if there is another even
#                 if even.next.next:
#                     next_even = even.next.next
#                     next_odd = even.next

#                     odd.next = next_even
#                     next_evens_next = next_even.next
#                     next_even.next = even.next
#                     next_odd.next = even
#                     even.next = next_evens_next

#                     odd = next_odd
#                 # if there is an odd left
#                 else:
#                     # update last node's next
#                     even.next.next = even
#                     # update even's next to end
#                     even.next = None

#                     even = None
                
#                 print(odd.val, even.val if even else None)

#             curr = curr.next
