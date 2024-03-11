# ************************************
# 二分查找
# ************************************
def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low<=high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess==item:
            return mid
        elif guess < item:
            low = mid+1
        else:
            high = mid-1
    return None
# ************************************
# 选择排序
# ************************************
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append((arr.pop(smallest)))
    return newArr
# print(selectionSort([5,3,6,2,10]))
def selection_sort2(arr):
    for i in range(len(arr)-1):
        smallest_index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[smallest_index]:
                smallest_index=j
        if i!=smallest_index:
            arr[i],arr[smallest_index] = arr[smallest_index],arr[i]

    return arr
# print(selection_sort2([5,3,6,2,10]))

# ******************************************************
# 快速排序
# 快速排序
# 快速排序
# *******************************************************

# 方法有几种
#方法一：用额外的存储空间来存储less和greater列表
def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less=[elem for elem in arr[1:] if elem<=pivot]
        greater = [elem for elem in arr[1:] if elem>pivot]

        return quickSort(less) +[pivot]+quickSort(greater)

#方法二：
# 假设当前排序为R[low:high]，其中low ≤ high。
#
# 1：首先取序列第一个元素为基准元素pivot=R[low]。i=low,j=high。
# 2：从后向前扫描，找小于等于pivot的数，如果找到，R[i]与R[j]交换，i++。
# 3：从前往后扫描，找大于pivot的数，如果找到，R[i]与R[j]交换，j--。
# 4:重复2~3，直到i=j,返回该位置mid=i,该位置正好为pivot元素。
# 完成一趟排序后，以mid为界，将序列分为两部分，左序列都比pivot小，有序列都比pivot大，然后再分别对这两个子序列进行快速排序。
def quickSorttest(arr, i, j):
    if i >= j:
        return arr
    pivot = arr[i]
    low = i
    high = j
    while i < j:
        while i < j and arr[j] >= pivot:
            j = j - 1
        arr[i]=arr[j]
        while i < j and arr[i] <= pivot:
            i = i + 1
        arr[j]=arr[i]
    arr[j] = pivot
    quickSorttest(arr, low, i - 1)
    quickSorttest(arr, i + 1, high)
    return arr
# print(quickSorttest([2,5,6,1,3,9],0,5))

# 队列是一种先进先出(First In First Out,FIFO)的数据结构，而栈是一种后进先出(Last In First Out,LIFO)的数据结构。
# 知道队列的工作原理后，我们来实现广度优先搜索！


