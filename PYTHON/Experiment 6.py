class CircularQueue:
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
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity
            print()


# Example usage of CircularQueue
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()
cq.enqueue(5)
cq.enqueue(6)
cq.display()



def linear_search(arr, key):
    for i, item in enumerate(arr):
        if item == key:
            return i
    return -1

def binary_search(arr, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, key, mid + 1, high)
        else:
            return binary_search(arr, key, low, mid - 1)
    else:
        return -1

# Example usage of search functions
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 5
linear_result = linear_search(arr, key)
print(f"Linear Search: Element {key} found at index {linear_result}.")

binary_result = binary_search(arr, key, 0, len(arr) - 1)
print(f"Binary Search: Element {key} found at index {binary_result}.")
