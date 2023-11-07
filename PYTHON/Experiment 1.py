class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to create a new node and add it to the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Function to delete a node with a specific value from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next

    # Function to traverse and print the elements of the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Function to create a linked list from a list of elements
def create_linked_list(elements):
    linked_list = LinkedList()
    for element in elements:
        linked_list.insert(element)
    return linked_list

if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5])

    print("Linked List:")
    linked_list.traverse()

    linked_list.insert(6)
    print("After insertion of 6:")
    linked_list.traverse()

    linked_list.delete(3)
    print("After deletion of 3:")
    linked_list.traverse()
