_author_ = 'Nikita Karatsev'
_project_ = 'Lab2'

import DoubleLinkedList
from notebook.notebookapp import raw_input

d1 = DoubleLinkedList.DoubleLinkedList()
d2 = DoubleLinkedList.DoubleLinkedList()
ifs = ''
'''a = {"0": d.fill_deque(),
         "1": d.sort1(),
         "2": d.sort2(),
         "3": d.sort3()
    }
'''
while ifs is not '~':
    #"Welcome. 0 - add deque, 1-3 sort seque, ~ exit")
    print(
    "\nДобро пожаловать в консоль. Что будем делать?!(0 - заполнить массив, 1..3 - сортировка и вывод на экран)")
    ifs = raw_input()
    if ifs is '0':
        d1.fill_deque(d2)
    elif ifs is '1':
        d1.sort1(d2)
    elif ifs is '2':
        d1.sort2(d2)
    elif ifs is '3':
        d1.sort3(d2)
    elif ifs is '~':
        print("FBI OPEN DOOR!")
    else:
        print("Неверно введена цифра(~ - выход)")
    # a[ifs]