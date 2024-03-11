# 二叉堆
# 插入节点
## 插入位置是完全二叉树的最后一个位置
## 和父节点比较，比父节点小，则节点上浮，与父节点交换


#删除节点
## 删除的是处于堆顶的节点
## 为了维持完全二叉树的结构，把最后一个节点临时补到堆顶
## 接下来父节点与左右孩子比较，如果左右孩子节点中的较小者比父节点小，则父节点下沉


#构建二叉堆
## 本质就是让所有非叶节点依次下沉
## 从最后一个非叶子节点开始，下沉


# 父节点下表parent，则左右孩子的下标为 2*parent +1，2*parent+2

#上浮节点

def upAdjust(arr):
    childIndex = len(arr)-1
    parentIndex = (childIndex-1)//2
    temp = arr[childIndex]
    while childIndex>0 and temp<arr[parentIndex]:
        arr[childIndex]=arr[parentIndex]
        childIndex=parentIndex
        parentIndex=(childIndex-1)//2
    arr[childIndex]=temp

def downAdjust(arr,parentIndex,length):
    temp = arr[parentIndex]
    childIndex = parentIndex*2 +1
    while childIndex<length:
        if childIndex+1<length and arr[childIndex+1] < arr[childIndex]:
            childIndex += 1
        if temp <=arr[childIndex]:
            break
        arr[parentIndex]=arr[childIndex]
        parentIndex = childIndex
        childIndex = childIndex *2 +1
    arr[parentIndex]=temp

def buildHeap(arr):
    length = len(arr)
    for i in range((length-2)//2,-1,-1):
        downAdjust(arr,i,length)

array = [1,3,2,6,5,7,8,9,10,0]
buildHeap(array)
print(array)