class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_from_stack(self, element):
        found = False
        temp_stack = Stack()
        result = None

        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                result = item
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Element '{element}' not found in the stack.")

        return result



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)



    try: 
        user_char = int(input("Print a number: "))
    except ValueError as e:
        print(e)

    try:
        element = stack.get_from_stack(user_char)
        print("Element found:", element)
    except ValueError as e:
        print(e)

    try:
        element = stack.get_from_stack(5)
        print("Element found:", element)
    except ValueError as e:
        print(e)