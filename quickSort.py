

def quickSort(array,startIndex,endIndex):
    if startIndex>=endIndex:
        return

    # pivotIndex = partition(array,startIndex,endIndex)
    pivotIndex = partitionSingle(array,startIndex,endIndex)
    quickSort(array,startIndex,pivotIndex-1)
    quickSort(array,pivotIndex+1,endIndex)

# 用left 和right 两个指针
def partition(arr,startIndex,endIndex):
    #取第一个元素为pivot
    pivot = arr[startIndex]
    left = startIndex
    right = endIndex

    while left!=right:
        while left<right and arr[right]>pivot:
            right -=1
        while left<right and arr[left]<=pivot:
            left +=1
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]

    arr[startIndex]=arr[left]
    arr[left]=pivot
    return left

# 用一个指针
def partitionSingle(arr,startIndex,endIndex):
    pivot = arr[startIndex]
    mark = startIndex

    for i in range(startIndex+1,endIndex+1):
        if arr[i]<pivot:
            mark +=1
            arr[mark],arr[i]=arr[i],arr[mark]

    arr[startIndex]=arr[mark]
    arr[mark]=pivot
    return mark



list = [4,4,6,5,3,2,8,1]

quickSort(list,0,len(list)-1)
print(list)