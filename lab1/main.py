_author_ = 'Nikita Karatsev'
_project_ = 'Lab1'

import mymodule

# для ввода значений(raw_input, хз почему так не работает)


# проверяем работу алгоритма
l = mymodule.LinkedList()

string = raw_input("Введите строку: ")
for i in range(len(string)):
    l.add(string[i])

l.str_result()
print(l)
