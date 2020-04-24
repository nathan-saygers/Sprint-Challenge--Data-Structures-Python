from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if self.storage.length is less than capacity
        if self.storage.length < self.capacity:
            # add the item to the head
            self.storage.add_to_tail(item)
        else:
            if self.current == None:
                self.storage.head.value = item
                self.current = self.storage.head.next
            else:
                self.current.value = item
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head

        # Traverse the doubly linked list
        # while there is a next value
        while current_node:
            # push current node onto list buffer contents
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        # TODO: Your code here
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# tester = RingBuffer(5)

# tester.append('a')
# tester.append('b')
# tester.append('c')
# tester.append('d')
# tester.append('e')
# tester.append('f')
# tester.append('f')

# print(tester.storage.head.value, tester.storage.length)
# print(tester.get())