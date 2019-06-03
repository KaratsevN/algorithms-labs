#from node import *
_author_ = 'Nikita Karatsev'
_project_ = 'Lab4'

from tree import *
# для ввода значений(raw_input, хз почему так не работает)
from notebook.notebookapp import raw_input


def main():
    mytree = BinarySearchTree()
    i = 0
    c = '_'
    while (c != '~'):
        print(
            "Добро пожаловать. -1 - заполнить автоматом, 0 - добавить, "\
            "1 - число вершин на n-ом уровне,  2 - высота дерева, ~ - выход.")
        c = raw_input("Введите: ")
        if c == '-1':
            mytree.put(5)
            mytree.put(3)
            mytree.put(7)
            mytree.put(2)
            mytree.put(4)
            mytree.put(6)
            mytree.put(8)
            mytree.put(9)
            mytree.put(10)
        if (c == '0'):
            i = int(raw_input("Введите значение: "))
            mytree.put(i)
        elif (c == '1'):
            mytree.level = mytree.height()
            i = int(raw_input("Введите уровень: "))
            mytree.peaks = mytree.sizeTree(i, mytree.root)
            if mytree.peaks == -1:
                print("Некорректное значение(высота дерева меньше)")
            else:
                print("Число вершин: ", mytree.peaks)
        elif (c == '2'):
            mytree.level = mytree.height()
            print(mytree.level)
        elif (c == '~'):
            print("You say goodbye and I say hello!")


if __name__ == '__main__':
     main()