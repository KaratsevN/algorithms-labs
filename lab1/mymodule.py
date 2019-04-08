import random
import math

# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'LinkedList []'

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
        curr = self.first
        count = 0
        # self.length = 0
        if i == 0:
            self.first = self.first.next
            self.length -= 1
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                self.length -= 1
                break
            old = curr
            curr = curr.next
            count += 1

    def str_result(self):
        repeat = False
        i = 0
        j = 0
        current = self.first
        curr = self.first
        while i < self.length - 1:
            j = i + 1
            while j < self.length:
                if (curr.next != None):
                    curr = curr.next
                    if i != j and current.value == curr.value:
                        self.Del(j)
                        j = j - 1
                        repeat = True
                j += 1
            if (repeat):
                self.Del(i)
                if (i != 0):
                    i = 0
                repeat = False
                current = self.first
                curr = self.first
            else:
                current = current.next
                curr = current
                i += 1
        return
