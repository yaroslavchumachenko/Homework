from my_node import Node

class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"
    
    def append(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                print(index)
                return index
            current = current.get_next()
            index += 1
        raise ValueError(f"{item} not in list")
       

    def pop(self, index=None):
        if index is None:
            if self._head is None:
                raise IndexError("pop from empty list")
            elif self._head.get_next() is None:
                item = self._head.get_data()
                self._head = None
                return item
            else:
                current = self._head
                while current.get_next().get_next() is not None:
                    current = current.get_next()
                item = current.get_next().get_data()
                current.set_next(None)
                return item
        elif index == 0:
            if self._head is None:
                raise IndexError("pop from empty list")
            else:
                item = self._head.get_data()
                self._head = self._head.get_next()
                return item
        else:
            current = self._head
            previous = None
            current_index = 0
            while current_index < index and current is not None:
                previous = current
                current = current.get_next()
                current_index += 1
            if current is None:
                raise IndexError("pop index out of range")
            else:
                item = current.get_data()
                previous.set_next(current.get_next())
                return item

    def insert(self, index, item):
        if index == 0:
            new_node = Node(item)
            new_node.set_next(self._head)
            self._head = new_node
        else:
            current = self._head
            current_index = 0
            while current_index < index - 1 and current is not None:
                current = current.get_next()
                current_index += 1
            if current is None:
                raise IndexError("insert index out of range")
            else:
                new_node = Node(item)
                new_node.set_next(current.get_next())
                current.set_next(new_node)

    def slice(self, start, stop):
        if start >= stop:
            return []
        
        current = self._head
        index = 0
        sliced_list = []
        while current is not None and index < stop:
            if index >= start:
                sliced_list.append(current.get_data())
            current = current.get_next()
            index += 1
        return sliced_list

    
if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))
    print(my_list.slice(0,4))
    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())
    my_list.append(111)
    my_list.index(111)


    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    print(my_list)
    my_list.index(77)
    my_list.pop(1)
    print(my_list)
    my_list.insert(1, 15)
    print(my_list)
    