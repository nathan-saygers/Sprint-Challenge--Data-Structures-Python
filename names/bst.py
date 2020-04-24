class BinarySearchTreeNode:
    # Note about class name: it's more of a BST NODE than a tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty (can park)
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        # otherwise value is >= self.value
        else:
            if self.right:
                self.right.insert(value)
            # if no right hand value
            else:
                self.right = BinarySearchTreeNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if value is target
        if target == self.value:
            return True
        # self.left and/or self.right need to be valid nodes
        # for us to call contains on them
        if target < self.value:
            # check if self.left is a valid node
            if self.left:
                return self.left.contains(target)
            else:
                return False
        # otherwise target is >= self.value
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check if the current node has a self.right
        if self.right:
            # if yes: call get_max again
            return self.right.get_max()
        # if no: return self.value
        else:
            return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Use the callback on the self.value of the current node
        self.value = cb(self.value)
        # Check to see if there is a self.left
        if self.left:
            # Call again on self.left
            self.left.for_each(cb)
        # Check to see if there is a self.right
        if self.right:
            # Call again on self.right
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack 
        stack.append(self)
        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)