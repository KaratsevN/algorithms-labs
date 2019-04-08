import sys
from itertools import groupby

# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input

_author_ = 'Nikita Karatsev'
_project_ = 'Lab1'

str = ''
l = 0
i = 0
j = 0
def enter_str():
    str = raw_input('Введите строку: ')
    #str = list(str)
    return str

def str_result(str, l):
    count = 0
    for i in range(0,l):
        count = 0
        for j in range(0,l):
            if(i!=j and str[i] == str[j]):
                count = count+1
        if(count>=1):
            None
        else:
            print(str[i])

def str_result_normal(str, l):
    for i in range(len(str)):
        for j in range(len(str)):
            if i != j and str[i] == str[j]:
                break
        else:
            print(str[i], end=' ')

def str_result_easy(str, l):
    new_x = [i for i, _ in groupby(str)]
    print(new_x)

#ну это же питон!
def str_result_supereasy(str):
    newstr = set(str)
    print(str)

str = enter_str()
l = len(str)
str_result(str, l)
print('=====================================')
str_result_normal(str, l)
print('=====================================')
str_result_supereasy(str)
#str_result_easy(str, l)
#iterator_str(str, l, i, j)

