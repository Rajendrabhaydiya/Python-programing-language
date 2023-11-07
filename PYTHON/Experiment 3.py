class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        elif position == 0:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
                if temp == self.head:
                    print("Invalid position.")
                    return
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:
            temp = self.head
            prev = None
            found = False
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == key:
                    found = True
                    break
            if found:
                prev.next = temp.next
            else:
                print("Key not found in the list.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.create(1)
    cll.create(2)
    cll.create(3)
    cll.create(4)

    print("Circular Linked List:")
    cll.display()

    cll.insert(0, 0)
    cll.insert(5, 5)
    cll.insert(2.5, 2)

    print("Circular Linked List after insertions:")
    cll.display()

    cll.delete(0)
    cll.delete(5)
    cll.delete(2.5)

    print("Circular Linked List after deletions:")
    cll.display()
