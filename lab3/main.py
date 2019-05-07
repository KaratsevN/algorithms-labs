_author_ = 'Nikita Karatsev'
_project_ = 'Lab1'
#Contribution activity wasn't displayed on GitHub so I made this commit with this comment.
import queue1
# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input

c = ' '
key = ''
string = ""
i = 0

# проверяем работу алгоритма
l = queue1.Queue1()
# menu = {'0': inputvar(string),
#         '1':l.add(key),
#         '2':l.Del(i),
#         '3': l.InsertNth(i, key),
#         '4': l.__str__(),
#         '~': print("You say goodbye and I say hello!")}

while(c != '~'):
    print("Добро пожаловать. 0 - заполнить очередь, 1 - добавить, 2 - удалить,  3 - вывод на экран. 4 - длинна, ~ - выход.")
    c = raw_input("Введите: ")
    if(c == '0'):
        string = raw_input("Введите значение: ")
        for i in range(len(string)):
            l.add(string[i])
    elif(c =='1'):
        key = input("Введите key: ")
        l.add(key)
    elif(c =='2'):
        i = int(input("Введите i: "))
        l.Del(i)
    # elif(c =='3'):
    #     i = int(input("Введите i: "))
    #     key = input("Введите key: ")
    #     l.InsertNth(i, key)
    elif(c =='3'):
        print(l)
    elif (c == '4'):
        l.__len__()

    elif(c =='~'):
        print("You say goodbye and I say hello!")
    #menu[c]
    #l.str_result()
