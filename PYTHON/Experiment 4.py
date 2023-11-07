class StackUsingArray:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        if not self.is_empty():
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            print("Stack is empty. Cannot pop item.")

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            print("Stack is empty. No item to peek at.")

# Example usage of Stack using Arrays
stack = StackUsingArray(5)
stack.push(1)
stack.push(2)
stack.push(3)
print("Top item:", stack.peek())  # Output: Top item: 3
print("Popped item:", stack.pop())  # Output: Popped item: 3