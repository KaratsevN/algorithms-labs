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

    def fill_deque(self, deque):
        string = raw_input("Введите строку: ")
        for i in range(0, len(string)):
            self.add(string[i])
            deque.add(string[i])

    def sort1(self, deque):
        current_node = self.head
        curr = deque.tail
        while current_node is not None:
            deque.add(current_node.data)
            current_node = current_node.next
        #while current_node.next is not None:
        #    current_node = current_node.next
        curr = deque.head
        while curr is not None:
            if curr.next is None:
                print(curr.data, end="")
                break
            else:
                print(curr.data, end=" <-> ")
                curr = curr.next
        #current_node = self.head
        #while current_node is not None:
        #    if current_node.next is None:
        #        print(current_node.data, end=" <-> ")
        #        break
        #    else:
        #        print(current_node.data, end=" <-> ")
        #        current_node = current_node.next
        pass

    def sort2(self, deque):
        #helper = 0
        if deque.len_of() is not self.len_of():
            curr1 = deque.head
            curr2 = deque.tail
            for i in range(0, self.len_of()):
                curr2.data = curr1.data
                curr1 = curr1.next
                curr2 = curr2.prev
        else:
            current_node = self.tail
            while current_node is not None:
                deque.add(current_node.data)
                current_node = current_node.prev
        curr1 = deque.head
        while curr1 is not None:
            if curr1.next is None:
                print(curr1.data, end="")
                break
            else:
                print(curr1.data, end=" <-> ")
                curr1 = curr1.next
        # curr = deque.tail
        # current_node = self.tail
        # while current_node is not None:
        #     if current_node.prev is None:
        #         deque.add(current_node.data)
        #         curr = curr.next
        #         print(curr.data, end="")
        #         #print(current_node.data, end=" , ")
        #         break
        #     else:
        #         deque.add(current_node.data)
        #         curr = curr.next
        #         print(curr.data, end=" <-> ")
        #     current_node = current_node.prev
        pass

    def sort3(self, deque):
        if deque.len_of() is self.len_of():
            current = deque.head
            current1 = self.head
            current2 = self.tail
            for i in range(0, self.len_of()):
                current.data = current2.data
                deque.add(current1.data)
                current = current.next
                current1 = current1.next
                current2 = current2.prev
        else:
            current = self.tail
            current1 = deque.head
            current2 = deque.tail
            for i in range(0, self.len_of()):
                current1.data = current.data
                current2.data = current1.data
                current = current.prev
                current1 = current1.next
                current2 = current2.prev
        current1 = deque.head
        while current1 is not None:
            if current1.next is None:
                print(current1.data, end="")
                break
            else:
                print(current1.data, end=" <-> ")
                current1 = current1.next
        # current_node = self.head
        # while current_node is not None:
        #     if current_node.next is None:
        #         print(current_node.data, end=" , ")
        #         break
        #     else:
        #         print(current_node.data, end=" <-> ")
        #         current_node = current_node.next
        pass
