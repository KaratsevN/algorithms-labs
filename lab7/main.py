_author_ = 'Nikita Karatsev'
_project_ = 'Lab7'

from data import *


def addPerson(name, age):
    data.append({
        'name': name,
        'age': age
    })

def printPerson(retirement_age):
    print('На пенсию уходят: ')
    for i in range(0, len(data)):
        if(data[i]['age'] >= retirement_age):
            print('ФИО: {} \n Возраст: {}'.format(data[i]['name'], data[i]['age']))

def sortPerson():
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j]['age'] < data[j + 1]['age']:
                data[j], data[j + 1] = data[j + 1], data[j]

def main():
    c = ' '
    name = ""
    while (c != '~'):
        print("Добро пожаловать. 0 - новый студент, 1 - вывод на экран, 2 - сортировка, ~ - выход.")
        c = input("Введите: ")
        if (c == '0'):
            name = input("ФИО: ")
            age = input("Дата рождения(в формате ДД, ММ, ГГГГ): ")
            addPerson(name, age)
        if c == '1':
            retirement_age = int(input("Введите пенсионнный возраст: "))
            printPerson(retirement_age)
        if c == '2':
            sortPerson()


if "__main()__" == main():
    main()