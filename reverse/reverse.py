# #### Task 3. Reverse a Linked List

# Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list using recursion, *not a loop.*

# For example,
# ```
# 1->2->3->None
# ```
# would become...
# ```
# 3->2->1->None
# ```

# While credit will be given for a functional solution, only optimal solutions will earn a ***3*** on this task.

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return
        
        # store current node's next value (1 saves 2 in [1, 2, 3, 4, 5])
        next_node = node.get_next()

        # set current node's next value to previous value. swapping it behind the current node (1 puts two behind it now [2, 1, 3, 4, 5])
        node.set_next(prev)

        # check if next node exists
        if next_node is not None:
            # recursively call the function 
            self.reverse_list(next_node, node)
        else:  # if there is no next node, we've reached the end
            # set the new head node
            self.head = node
