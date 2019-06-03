_author_ = 'Nikita Karatsev'
_project_ = 'Lab3'

import random
import math

# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue1:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'Queue [' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'Queue []'

    def __len__(self):
        print(self.length)

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def InsertNth(self, i, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next

    # удаление элемента
    def Del(self, i):
        if (self.first == None):
            return
        # curr = self.first
        # count = 0
        self.first = self.first.next
        # self.length = 0
        # if i == 0:
        #     self.first = self.first.next
        #     self.length -= 1
        #     return
        # while curr != None:
        #     if count == i:
        #         if curr.next == None:
        #             self.last = curr
        #         old.next = curr.next
        #         self.length -= 1
        #         break
        #     old = curr
        #     curr = curr.next
        #     count += 1
