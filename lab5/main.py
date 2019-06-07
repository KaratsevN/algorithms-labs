_author_ = 'Nikita Karatsev'
_project_ = 'Lab5'

# this comment is made for Github statistic(sorry, but I doing other things today). I'll be more productive.

# Contribution activity wasn't displayed on GitHub so I made this commit with this comment.

# для ввода значений(raw_input, хз почему так не работает)
# from notebook.notebookapp import raw_input

# import json

import datetime
from data import data

'''
struct = """[
    {
      "first_name": "lol",
      "last_name": "",
      "birthdate": 0,
      "estimates": {
        "algorithms": 0,
        "maths": 0,
        "physics": 0,
        "programming": 0,
        "total": 0
      }
    },
    {
      "first_name": "lol",
      "last_name": "",
      "birthdate": 0,
      "estimates": {
        "algorithms": 0,
        "maths": 0,
        "physics": 0,
        "programming": 0,
        "total": 0
      }
    }
]
"""
'''


def addStudent(dname, dbirthdate, destimates):
    data.append(dict(name=dname, birthdate=datetime.datetime.strptime(dbirthdate, '%d%m%Y'),
                     estimates=dict(
                         algorithms=destimates[0],
                         maths=destimates[1],
                         physics=destimates[2],
                         programming=destimates[3],
                         total=float(sum(destimates) / len(destimates))
                     ))
                )


def printStudents():
    for i in range(0, len(data)):
        # print("name: {} \n birthdate: {} \n algorithms: {} \n maths: {} \n phys: {} \n programming: {} \n total: {}").format(
        print("ФИО: ", data[i]['name'], end='\n')
        print("Дата рождения: ", data[i]['birthdate'].strftime("%d/%m/%Y"), end='\n')
        print("  Алгоритмы:        ", data[i]['estimates']['algorithms'], end='\n')
        print("  Математика:       ", data[i]['estimates']['maths'], end='\n')
        print("  Физика:           ", data[i]['estimates']['physics'], end='\n')
        print("  Программирование: ", data[i]['estimates']['programming'], end='\n')
        print("  Всего:            ", data[i]['estimates']['total'])
        print("======================================")


def sortStudents():
    helper = data[0]
    for i in range(0, len(data) - 1):
        small = i
        for j in range(i + 1, len(data)):
            if data[small]['birthdate'] < data[j]['birthdate']:
                small = j
            data[i], data[small] = data[small], data[i]


def main():
    c = ' '
    name = ""
    while (c != '~'):
        print("Добро пожаловать. 0 - новый студент, 1 - вывод на экран, 2 - сортировка, ~ - выход.")
        c = input("Введите: ")
        if (c == '0'):
            name = input("ФИО: ")
            birthdate = input("Дата рождения(в формате ДД, ММ, ГГГГ): ")
            estimates = [int(input("Оценки(алгоритмы, высш матан, физика, программирование): ")) for i in range(0, 4)]
            addStudent(name, birthdate, estimates)
            # print(arr)
        if c == '1':
            printStudents()
        if c == '2':
            sortStudents()


if "__main()__" == main():
    main()
