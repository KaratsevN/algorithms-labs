from node import *


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.lvl = 0
        self.treeroot = self.root

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


    def copy_route(self):
        self.treeroot = self.root


    def size_size(self, level = 0, root = None):
        if root is None:
            self.lvl = 1
            return self.lvl
        else:
            return self.size_size(level, self.root.left) + 1 + self.size_size(level, self.root.right)
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