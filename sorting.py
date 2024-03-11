

#十大排序
# 1、冒泡排序
# 2、选择排序
# 3、插入排序
# 4、希尔排序
# 5、归并排序
# 6、快速排序
# 7、堆排序
# 8、计数排序
# 9、桶排序
# 10、基数排序
testarr = [2,5,3,1,10,4]

#1.冒泡排序
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#2.选择排序
def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        if i!=minIndex:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr

#3.插入排序
def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1]=arr[preIndex]
            preIndex=preIndex-1
        arr[preIndex+1]=current
    return arr

#5.归并排序
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left,right = arr[0:middle],arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result=[]
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# 6、快速排序
def quickSort(arr,i,j):
    if i>=j:
        return arr
    pivot = arr[i]
    low = i
    high = j
    while i<j:
        while i<j and arr[j]>=pivot:
            j=j-1
        arr[i]=arr[j]
        while i<j and arr[i]<=pivot:
            i=i+1
        arr[j]=arr[i]
    arr[j]=pivot
    quickSort(arr,low,i-1)
    quickSort(arr,i+1,high)
    return arr

def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quickSortNew(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quickSortNew(arr,low,pi-1)
        quickSortNew(arr,pi+1,high)
    return arr

# 7、堆排序

def heapify(arr,n,i):
    if i >= n:
        return
    max=i
    c1 = 2*i+1
    c2 = 2*i+2

    if c1<n and arr[max]<arr[c1]:
        max = c1
    if c2<n and arr[max]<arr[c2]:
        max = c2

    if max!=i:
        arr[i],arr[max]=arr[max],arr[i]
        heapify(arr,n,max)

def buildHeap(arr):
    n=len(arr)
    last_node = n - 1
    parent = int((last_node - 1) / 2)
    for i in range(parent,-1,-1):
        heapify(arr,n,i)
    return arr

def heapSort(arr):
    n=len(arr)
    buildHeap(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

print(heapSort(testarr))


