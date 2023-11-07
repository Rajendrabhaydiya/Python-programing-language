class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity

    def front_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - (self.front - self.rear) + 1


# Example usage:
queue = ArrayQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Front:", queue.front_element())
print("Size:", queue.size())
queue.dequeue()
print("Front after dequeue:", queue.front_element())



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next

    def front_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Front:", queue.front_element())
print("Size:", queue.size())
queue.dequeue()
print("Front after dequeue:", queue.front_element())
