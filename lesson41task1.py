class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

def reverse_char(user_str):
    stack = Stack()
    for char in user_str:
        stack.push(char)
    
    reversed_string = ""
    while stack.is_empty():
        reversed_string += stack.peek()
        stack.pop()
        print(stack)
    
    return reversed_string

if __name__ == "__main__":
    input_string = input("Enter a sequence of characters: ")
    reversed_string = reverse_char(input_string)
    print("Reversed sequence:", reversed_string)
    