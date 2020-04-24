class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # If previous is not none:
        if node != None:
            if node.next_node == None:
                self.head = node
                node.next_node = prev
                return
            # call function again with curr and next as node and prev
            self.reverse_list(node.next_node, node)
            # set Node.next to be previous
            if prev != None:
                node.next_node = prev
            else:
                node.next_node = None
        
        #Things that need to happen:
            # 1 points to 2 points to 3 etc
            # old next links are severed
            # head is transferred to 1

# For example,
# ```
# 5 <- 4 -> 3 -> 2 <-> 1 -> None
#                N
#          P
# H



# would become...
# ```
# 3 <- 2 <- 1 <- None
# ```

tester = LinkedList()

tester.add_to_head(1)
tester.add_to_head(2)
tester.add_to_head(3)
tester.reverse_list(tester.head, None)