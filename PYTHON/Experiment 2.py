class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not provided.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Create a doubly linked list
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)

# Display the initial list
print("Initial Doubly Linked List:")
dllist.display()

# Insert a node after a given node
dllist.insert_after(dllist.head.next, 4)
print("Doubly Linked List after inserting 4:")
dllist.display()

# Delete a node
dllist.delete(2)
print("Doubly Linked List after deleting 2:")
dllist.display()
