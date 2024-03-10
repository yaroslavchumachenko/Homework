from my_node import Node

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            item = self._head.get_data()
            self._head = self._head.get_next()
            if self._head is None:
                self._tail = None
            return item

    def peek(self):
        if self.is_empty():
            raise IndexError("It's empty")
        else:
            return self._head.get_data()

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


print(queue.size())

print(queue.peek()) 

print(queue.dequeue()) 
print(queue.size())