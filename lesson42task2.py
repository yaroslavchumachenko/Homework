from my_node import Node

class Stack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            item = self._head.get_data()
            self._head = self._head.get_next()
            return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self._head.get_data()

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.size())

print(stack.peek())

print(stack.pop())
print(stack.size())