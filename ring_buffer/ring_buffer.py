from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.total_counter = self.storage.length

    def append(self, item):
        # if self.storage.length is less than capacity
        if self.storage.length < self.capacity:
            # add the item to the head
            self.storage.add_to_tail(item)
            self.total_counter += 1
        # if self.storage.length is equal to capacity
        if self.total_counter % capacity == 0:
            # pop off the tail
            self.storage.remove_from_tail()
            self.storage.length += 1
            self.total_counter += 1
            # add the item after the head
            self.storage.head.insert_after(item)
            # swap the head with its next
            temp = self.storage.head.value
            self.storage.head.value = self.storage.head.next.value
            self.storage.head.next.value = temp
        else:
            self.storage.remove_from_tail()
            self.storage.length += 1
            self.total_counter += 1
            

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


tester = RingBuffer(5)

tester.append('a')
tester.append('b')
tester.append('c')
tester.append('d')
tester.append('e')
tester.append('f')
tester.append('f')

print(tester.storage.head.value, tester.storage.length)
print(tester.get())