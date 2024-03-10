class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

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

def is_balanced(expression):
    stack = Stack()
    opening_brackets = "({["  # Opening brackets
    closing_brackets = ")}]"  # Closing brackets

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return stack.is_empty()

if __name__ == "__main__":
    sequence = input("Enter a sequence of parentheses, braces, and curly brackets: ")
    if is_balanced(sequence):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")