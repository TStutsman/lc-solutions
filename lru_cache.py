class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def move_to_tail(self, llist):
        if not self.next:
            return

        self.prev.next = self.next
        self.next.prev = self.prev

        llist.tail.next = self
        self.prev = llist.tail
        llist.tail = self
        self.next = None
    
class LRUList:
    def __init__(self):
        dummy = ListNode(None, None)
        self.head = dummy
        self.tail = dummy
    
    def add_node(self, key, value) -> ListNode:
        node = ListNode(key, value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        return node

    def remove_oldest(self) -> int:
        expired = self.head.next

        self.head.next = expired.next
        if expired.next:
            expired.next.prev = self.head
        else:
            self.tail = self.head

        return expired.key

class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.lru_list = LRUList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        # the store points to the node for O(1)
        node = self.store[key]
        node.move_to_tail(self.lru_list)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            # grab node from store
            node = self.store[key]

            # update value and list position
            node.value = value
            node.move_to_tail(self.lru_list)
            return


        node = self.lru_list.add_node(key, value)
        self.store[key] = node
        self.capacity -= 1

        if self.capacity < 0:
            expired_key = self.lru_list.remove_oldest()

            # remove lru from store
            del self.store[expired_key]
            
# class ListNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#         self.prev = None
    
#     def __repr__(self):
#         return "{ " + hex(id(self.prev)) + ' <==  <' + hex(id(self)) + '>  ==> ' + hex(id(self.next)) + ' }'

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.store = {}
#         dummy = ListNode(None, None)
#         self.head = dummy
#         self.tail = dummy
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.store:
#             return -1

#         # the store points to the node for O(1)
#         node = self.store[key]

#         # if the node isn't the tail (if it is it's already MRU)
#         if node.next:
#             node.prev.next = node.next
#             node.next.prev = node.prev

#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#             node.next = None

#         # print('get -', key, self.list_str())

#         return node.value
        

#     def put(self, key: int, value: int) -> None:
#         node = None

#         if key not in self.store:
#             # add new node
#             node = ListNode(key, value)
#             self.store[key] = node
#             self.capacity -= 1

#             if self.capacity < 0:
#                 expired = self.head.next

#                 # remove lru from store
#                 del self.store[expired.key]

#                 # remove lru from list
#                 self.head.next = expired.next
#                 if expired.next:
#                     expired.next.prev = self.head
#                 else:
#                     self.tail = self.head
#         else:
#             # update node's value
#             node = self.store[key]
#             node.value = value

#             node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev

#         # move node to end of list
#         self.tail.next = node
#         node.prev = self.tail
#         # update end of list pointer
#         self.tail = self.tail.next
#         node.next = None
#         print(node)
        
#         # print('put -', key, self.list_str())

#     def list_str(self):
#         p = []
#         curr = self.head.next

#         while curr:
#             p.append(str(curr.key) + ':' + str(curr.value))
#             curr = curr.next

#         return 'printing list\n' + ' => '.join(list(map(str, p)))

#     def store_str(self):
#         return "printing self.store\n" + '\n'.join(list(str(key) + ":" + str(value) for key,value in self.store.items()))