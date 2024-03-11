# 1.顺序查找
# 2.二分查找
# 3.插值查找
# 4.树表查找
# 5.分块查找
# 6.哈希查找
# 7.
#


# testList = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
# value = 66


def sequential_search(list, key):
    length = len(list)
    for i in range(length):
        if list[i] == key:
            return i
    return False


def binarySearch(arr, l, r, key):
    if r >= l:
        mid = int((l + r) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, l, mid - 1, key)
        else:
            return binarySearch(arr, mid + 1, r, key)
    else:
        return -1


# ***************二叉树*********************
# *************一起快活啊*******************

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    def printTree(self):
        print(self.data)

    #节点插入到树中
    def insert(self,data):
        #比较新值和父节点
        if self.data:
            if data<self.data:
                if self.lchild is None:
                    self.lchild=Node(data)
                else:
                    self.lchild.insert(data)
            elif data>self.data:
                if self.rchild is None:
                    self.rchild = Node(data)
                else:
                    self.rchild.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.lchild:
            self.lchild.printTree()
        print(self.data)
        if self.rchild:
            self.rchild.printTree()

Node_list=[12,6,14,3]
root = Node(Node_list[0])
for i in range(1,len(Node_list)):
    root.insert(Node_list[i])

root.printTree()







