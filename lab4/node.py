class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def height(self):
        return 1 + max(self.left.height() if self.left is not None else 0,
                       self.right.height() if self.right is not None else 0)