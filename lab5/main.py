_author_ = 'Nikita Karatsev'
_project_ = 'Lab5'
# Contribution activity wasn't displayed on GitHub so I made this commit with this comment.
# для ввода значений(raw_input, хз почему так не работает)
#from notebook.notebookapp import raw_input
import json
from data import data

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

def addStudent(name, birthdate, estimates):
    data['students'][0]['name'] = name
    data['students'][-1]['birthdate'] = birthdate
    data['students'][-1]['name'] = name
    data['students'][-1]['estimates']['algorithms'] = estimates[0]
    data['students'][-1]['estimates']['maths'] = estimates[1]
    data['students'][-1]['estimates']['physics'] = estimates[2]
    data['students'][-1]['estimates']['programming'] = estimates[3]
    data['students'][-1]['estimates']['total'] = sum(estimates) / len(estimates)

def printStudents():
    for i in range(0, len(data['students'])):
        print(data['students'][i]['name'])
        print(data['students'][i]['birthdate'])
        print(data['students'][i]['name'])
        print(data['students'][i]['estimates']['algorithms'])
        print(data['students'][i]['estimates']['maths'])
        print(data['students'][i]['estimates']['physics'])
        print(data['students'][i]['estimates']['programming'])
        print(data['students'][i]['estimates']['total'])

def main():
    c = ' '
    name = ""
    # arr[0] = 0
    while (c != '~'):
        print("Добро пожаловать. 0 - новый студент, 1 - вывод на экран, 2 - сортировка, ~ - выход.")
        c = input("Введите: ")
        if (c == '0'):
            string = input("ФИО: ")
            birthdate = input("Дата рождения(в формате ГГГГ, ММ, ДД): ")
            estimates = [int(input("Оценки(алгоритмы, высш матан, физика, программирование): ")) for i in range(0, 4)]
            addStudent(name, birthdate, estimates)
            #print(arr)
        if c == '1':
            printStudents()
    #data1 = json.loads(struct)
    # print(data1[0]["first_name"], end = '====')
    # print(data['students'][0]['first_name'])


if "__main()__" == main():
    main()
