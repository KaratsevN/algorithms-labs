from node import *

_author_ = 'Nikita Karatsev'
_project_ = 'Lab4'

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.level = 0
        self.peaks = 0
        #self.lvl = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = Node(key)
        self.size = self.size + 1

    def _put(self, key, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, currentNode.left)
            else:
                currentNode.left = Node(key, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, currentNode.right)
            else:
                currentNode.right = Node(key, parent=currentNode)

    def height(self):
        return self.root.height() - 1

    def sizeTree(self, level = 0, currRoot = None):
        if level > self.level:
            return -1
        if currRoot is None:
            return 0
        if level == 0:
            return 1
        return self.sizeTree(level - 1, currRoot.left) + self.sizeTree(level - 1, currRoot.right)
        #Мы писали, мы писали... Наши рученьки устали. Мы немного отдохнем и не будем удалять этот огрызок.
        # Так, на память как же тяжело было рекурсивно облапать дерево))
        '''
        Опасаясь контрразведки, 
        Избегая жизни светской,
        Под английским псевдонимом "мистер Джон Ланкастер Пек",
        Вечно в кожаных перчатках — 
        Чтоб не делать отпечатков, —
        Жил в гостинице "Совейской" несовейский человек.
        
        Джон Ланкастер в одиночку, 
        Преимущественно ночью,
        Щёлкал носом — в нём был спрятан инфракрасный объектив;
        А потом в нормальном свете 
        Представало в чёрном цвете
        То, что ценим мы и любим, чем гордится коллектив:
        
        Например, клуб на улице Нагорной 
        Стал общественной уборной,
        Наш родной Центральный рынок стал похож на грязный склад,
        Искаженный микроплёнкой, 
        ГУМ стал маленькой избёнкой,
        И уж вспомнить неприлично, чем предстал театр МХАТ.
        
        Но работать без подручных — 
        Может, грустно, а может — скучно.
        Враг подумал — враг был дока, — написал фиктивный чек,
        И где-то в дебрях ресторана 
        Гражданина Епифана
        Сбил с пути и с панталыку несовейский человек.
        
        Епифан казался жадным, 
        Хитрым, умным, плотоядным,
        Меры в женщинах и в пиве он не знал и не хотел.
        В общем так: подручный Джона 
        Был находкой для шпиона —
        Так случиться может с каждым, если пьян и мягкотел!
        '''
        # if self.lvl <= level:
        #     if currRoot.hasLeftChild():
        #         if self.lvl == level:
        #             self.peaks += 1
        #         self.lvl += 1
        #         self._sizeTree(level, currRoot.left)
        #         self.lvl -= 1
        #     else:
        #         if currRoot.hasRightChild():
        #             if self.lvl == level:
        #                 self.peaks += 1
        #             self.lvl += 1
        #             self._sizeTree(level, currRoot.right)
        #             self.lvl -= 1
        #         else:
        #             if self.lvl == level:
        #                 self.peaks += 1
        # if self.root.left is None and self.root.right is None:
        #     self.lvl += 1
        # # else:
        # #     self.lvl += 0
        # if self.root.left is not None:
        #     #root1 = sel
        #     self.lvl += self.print_peaks(level, self.root.left)
        # if self.root.right is not None:
        #     self.lvl += self.print_peaks(level, self.root.right)
        # return self.lvl
        # if self.treeroot is None:
        #     print('{}').format(self.lvl)
        #     return
        # else:
        #     CoutTerminal(tree * root)
        #     {
        #         size_t
        #     result;
        #     if ((root->left == NULL) & & (root->right == NULL)
        #             {
        #             result=1;
        #             }
        #             else
        #             {
        #             result=0;
        #             }
        #             if (root->left)
        #     {
        #     result += CoutTerminal(root->left);
        #     }
        #     if (root->right)
        #     {
        #     result += CoutTerminal(root->right);
        #     }
        #     return result;
        #     }
            #if self.treeroot.hasLeftChild() and self.treeroot.hasRightChild() is None:
                #self.copy_route()
            #else:
                # if self.treeroot.hasLeftChild() is not None:
                #     self.lvl += 1
                #     root = self.treeroot.hasLeftChild()
                #     self.print_peaks(level, root)
                # else:
                #     if self.treeroot.hasRightChild() is not None:
                #         self.lvl += 1
                #         self.print_peaks(level, self.treeroot.hasRightChild())
                #     else:
                #         pass
                    #self.treeroot = self.treeroot.hasLeftChild()
                    # if self.treeroot.hasLeftChild() is None:
                    #     #print(self.lvl)
                    #     if self.treeroot.hasLeftChild()
                #     else:
                #         self.treeroot = self.treeroot.hasLeftChild()
                #         self.print_peaks(level, self.treeroot)
                # else:
                #     if self.root.hasRightChild() is not None:
                #         self.lvl += 1
                #         if self.treeroot is None:
                #             print(self.lvl)
                #         else:
                #             self.treeroot = self.treeroot.hasRightChild()
                #             self.print_peaks(level, self.treeroot)
                #     else:
                #         print(self.lvl)
                #         return