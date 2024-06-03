# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # traverse both lists and add l1[i] + l2[i], store the LSD in new node
        # keep track of the overflow digit
        # repeat until no nodes left, if overflow still 1 add final node
        def _addRecursively(l1, l2, overflow):
            sum = 0
            next1, next2 = None, None
            if l1 and l2:
                sum = l1.val + l2.val + overflow
                next1, next2 = l1.next, l2.next
            elif l1:
                sum = l1.val + overflow
                next1 = l1.next
            elif l2:
                sum = l2.val + overflow
                next2 = l2.next
            elif overflow > 0:
                # Base cases
                final_node = ListNode(val = overflow)
                return final_node
            else:
                return None

            new_node = ListNode(val = sum % 10)
            new_overflow = sum // 10

            # Recursive step (travel to next node and recur)
            new_node.next = _addRecursively(next1, next2, new_overflow)

            return new_node
        
        return _addRecursively(l1, l2, 0)