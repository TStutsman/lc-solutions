from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # hash of visited {node: copy}
        # create head and copy val

        # update next and random pointers
            # if not visited yet, create new nodes to point to
        # move to the next node

        # return the copy of head
        # ===============================

        # Empty list check
        if not head: return

        # Initialize visited hash
        visited = { None: None, head: Node(head.val) }

        curr = head
        while curr:
            curr_copy = visited[curr]

            if curr.next not in visited:
                visited[curr.next] = Node(curr.next.val)

            curr_copy.next = visited[curr.next]

            if curr.random not in visited:
                visited[curr.random] = Node(curr.random.val)

            curr_copy.random = visited[curr.random]

            curr = curr.next
        
        return visited[head]