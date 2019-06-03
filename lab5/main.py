_author_ = 'Nikita Karatsev'
_project_ = 'Lab1'
#Contribution activity wasn't displayed on GitHub so I made this commit with this comment.
#import queue1
# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input
import datetime

c = ' '
name = ""
#arr[0] = 0
while(c != '~'):
    print("Добро пожаловать. 0 - заполнить очередь, 1 - вывод на экран, 2 - сортировка, ~ - выход.")
    c = raw_input("Введите: ", end = "\n")
    if(c == '0'):
        string = raw_input("ФИО: ")
        birthdate = raw_input("Дата рождения(в формате ГГГГ, ММ, ДД): ")
        arr = [raw_input("Оценки(алгоритмы, высш матан, физика, программирование): ") for i in range(0,4) ]
        print(arr)
    if c == '1':
        print()
