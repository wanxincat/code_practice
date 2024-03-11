# 1. 双指针: 只有一个输入, 从两端开始遍历
def fn(arr):
    left = ans = 0
    right = len(arr)-1

    while left < right:
         # 一些根据 letf 和 right 相关的代码补充
        if CONDITION:
            left += 1
        else:
            right -= 1
    return ans


#2. 双指针: 有两个输入, 两个都需要遍历完

def function(arr1,arr2):
    i = j = ans = 0
    while i < len(arr1) and j < len(arr2):
        if Condition:
            i += 1
        else:
            j +=1
    while i<len(arr1):
        i +=1
    while j<len(arr2):
        j +=1

    return ans


#3. 滑动窗口
def function(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # 根据题意补充代码来将 arr[right] 添加到 curr
        while Window_Condition_Broken:
            # 从 curr 中删除 arr[left]
            left +=1
        # 更新 ans
    return ans


#4. 构建前缀和
def function(arr):
    prefix = [arr[0]]
    for i in range(1,len(arr)):
        prefix.append(prefix[-1]+arr[i])
    return prefix


# 5. 高效的字符串构建
def function(arr):
    ans = []
    for c in arr:
        ans.append(c)
    return ''.join(ans)

#6. 链表: 快慢指针
def funtion(head):
    slow = fast = head
    ans = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return ans


#7. 反转链表
def function(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


#8. 找到符合确切条件的子数组数 ???
from collections import defaultdict
def function(arr,k):
    counts = defaultdict(int)
    counts[0]=1
    ans = curr = 0
    for num in arr:
        ans +=counts[curr-k]
        counts[curr] = counts[curr]+1
    return ans


#9. 单调递增栈
def function(arr):
    stack = []
    ans = 0
    for num in arr:
        while stack and stack[-1]>num:
            stack.pop()
        stack.append(num)
    return ans


#10. 二叉树: DFS (递归)
def dfs(root):
    if not root:
        return
    ans = 0
    # 根据题意补充代码
    dfs(root.left)
    dfs(root.right)
    return ans

#11. 二叉树: DFS (迭代)
def dfs(root):
    stack = [root]
    ans =0
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans

#12. 二叉树: BFS
from collections import deque
def function(root):
    queue = deque(root)
    ans =0
    while queue:
        current_length = len(queue)
        for _ in range(current_length):
            node = deque.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans

# 16. 找到堆的前 k 个元素
import heapq
def function(arr,k):
    for num in arr:
        # 做根据题意补充代码，根据问题的条件来推入堆中
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for num in heap]

#17. 二分查找
def function(arr,target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return
        if arr[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return left

# 18. 二分查找: 重复元素，最左边的插入点
def function(arr,target):
    left = 0
    right = len(arr)
    while left<right:
        mid = (left+right)//2
        if arr[mid]>=target:
            right = mid
        else:
            left = mid+1
    return left


def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
#20. 二分查找: 贪心问题
# 寻找最小值：
def fn(arr):
    def check(x):
        # 这个函数的具体实现取决于问题
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left
# 寻找最大值：

def fn(arr):
    def check(x):
        # 这个函数的具体实现取决于问题
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


# 21. 回溯
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # 修改答案
          return
    ans = 0
    for (ITERATE_OVER_INPUT):
        # 修改当前状态
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # 撤消对当前状态的修改
    return ans



