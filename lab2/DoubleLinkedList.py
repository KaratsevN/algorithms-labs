from notebook.notebookapp import raw_input

_author_ = 'Nikita Karatsev'
_project_ = 'Lab2'

class Node():

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data, None, None)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, num):
        count = 0
        current_node = self.head

        while True:
            if count == num:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
                break
            count += 1
            current_node = current_node.next

    def show(self):
        if self.head is None:
            print(None)
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data, end=" ")
                    break
                else:
                    print(current_node.data, end=" <---> ")
                    current_node = current_node.next

    def show_head(self):
        print(self.head)

    def len_of(self):
        current_node = self.head

        if current_node is None:
            return 0
        else:
            count = 0
            while current_node is not None:
                current_node = current_node.next
                count += 1
            return count

    def fill_deque(self):
        string = raw_input("Введите строку: ")
        for i in range(0, len(string)):
            self.add(string[i])

    def sort1(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                print(current_node.data, end=" <-> ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.next
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                print(current_node.data, end=" <-> ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.next
        pass

    def sort2(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                print(current_node.data, end=" , ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.next
        current_node = self.tail
        while current_node is not None:
            if current_node.prev is None:
                print(current_node.data, end=" , ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.prev
        pass

    def sort3(self):
        current_node = self.tail
        while current_node is not None:
            if current_node.prev is None:
                print(current_node.data, end=" , ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.prev
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                print(current_node.data, end=" , ")
                break
            else:
                print(current_node.data, end=" <-> ")
                current_node = current_node.next
        pass
