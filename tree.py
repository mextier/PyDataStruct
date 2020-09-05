"""class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
"""

class Tree:
    def __init__(self, data , left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def DataAsList(self, dir = -1):
        l = []
        l.append(None if self.left is None else self.left.data)
        l.append(None if self.right is None else self.right.data)
        if dir == -1:
            return l
        else:
            return l[::-1]

    def asList(self, tree, l = [], dir_ = - 1):
        if tree is None:
            return None
        else:
            l.append(tree.data)
            if dir_ == -1:
                self.asList(tree.left, l, dir_)
                self.asList(tree.right, l, dir_)
            else:
                self.asList(tree.right, l, dir_)
                self.asList(tree.left, l, dir_)

    def TreeAsList(self, dir_ = - 1):
        l = []
        while self.asList(self, l, dir_) is not None:
            pass
        return l

def isSymmetric(tree):
    if tree.left is None or tree.right is None:
        return False
    elif tree.left.data != tree.right.data:
        return False
    else:
        return tree.left.TreeAsList(-1) == tree.right.TreeAsList(1)


t = Tree(1,Tree(2,Tree(3),Tree(4)),Tree(2,Tree(4),Tree(3)))

print("!"*10)
print(t.DataAsList())
print("!"*10)
#print(t.left.TreeAsList())
#print(t.right.TreeAsList(1))
print(isSymmetric(t))
