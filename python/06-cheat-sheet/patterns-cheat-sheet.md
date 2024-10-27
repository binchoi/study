
# Notes from traversing the pattern roadmap
![patterns roadmap](patterns-roadmap.png)

# Table of Contents
1. [Arrays and Hashing](#Arrays-and-Hashing)
2. [Two Pointers)](#Two-Pointers)
3. [Stacks](#Stacks)
4. [Binary Search](#binary-search)

# Arrays and Hashing

## two sum
`(찾는 것) or (본 것) -> INDEX`

takeaways
- setting index as a value of a hashmap

## prefix sums
-> cumulative helper array
```python
def fillPrefixSum(arr, n, prefixSum):
    # first element = first element
    prefixSum[0] = arr[0]
 
    # subsequent elements = present + previous element
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
```

takeaways
- spending O(n) to initialize cumulative array when O(n) was required anyways such to make some consecutive addition calculations trivial
    - sum of 0 to i -> prefixSum[i]
    - sum from i to j -> prefixSum[j] - prefixSum[i-1]


# Two Pointers
## Complexity: O(n)
Three Sum questions are usually two-pointer questions (or 'three-pointer')

Left and right, moving inwards:
```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    res = collections.deque()
    l, r = 0, len(nums) - 1
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            res.appendleft(left * left)
            l += 1
        else:
            res.appendleft(right * right)
            r -= 1
    return list(res)
```

Both left to right, but one lagging behind (for-loop + variable)
```python
def removeDuplicates(self, nums: List[int]) -> int:        
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
```

Similarly, both left to right, same starting position; (for-loop + nested while-loop)
```python
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k < 2:
        return 0

    res = 0
    product = 1
    i = 0
    for j in range(len(nums)):
        product = product * nums[j]
        while i <= j and product >= k:
            product = product / nums[i]
            i += 1
        res += (j-i+1)
    return res
```


Three Pointers; one iterating over the iterator, two moving inward in remaining list from left/right
```python
def threeSumSmaller(self, nums: List[int], target: int) -> int:
    nums.sort()
    
    res = 0
    for i, n in enumerate(nums):
        j, k = i+1, len(nums)-1
        while j < k:
            curr_sum = n + nums[j] + nums[k]
            if curr_sum >= target:
                k -= 1
                continue
            res += (k-j)
            j += 1
    return res         
```

# Stacks

Be creative in what the format of the stack's elements to convey more information

e.g., (val, min_uptil_this)
```python
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append((val, val))
            return
        
        _, min_so_far = self.stk[-1]
        self.stk.append((val, min(min_so_far, val)))

    def pop(self) -> None:
        self.stk.pop()
        
    def top(self) -> int:
        val, _ = self.stk[-1]
        return val

    def getMin(self) -> int:
        _, curr_min = self.stk[-1]
        return curr_min
```

Think about what characteristic or trend your stack displays (e.g., at any point, the stack will contain temperatures in increasing order where max_temp is top)

(no need to use heapq to enforce this if using stacks in a particular way guarantees this trend)
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stk = []
    res = [0 for _ in temperatures]

    for i, t in enumerate(temperatures):
        while len(stk) > 0 and stk[-1][0] < t:
            _, j = stk.pop()
            res[j] = i-j
        stk.append((t, i))

    return res
```


# Binary Search



# Breadth-First Search (BFS)

**QUEUE** which at any given time contains nodes belonging to same level

- while q is not empty
- pop from q, N times where len(q) = N
- do operation; append its children if exists

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    q = deque()
    q.append(root)
    level = 0
    while len(q) > 0:
        level += 1
        level_node_count = len(q)
        for i in range(level_node_count):
            n = q.popleft()
            if n.left is None and n.right is None:
                return level
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
    return -1
```











# Dynamic Programming

tip: use `@cache` when you can
```python
from functools import cache

def maxSubArray(self, nums: List[int]) -> int:
    @cache
    def solve(i, must_pick):
        if i >= len(nums): return 0 if must_pick else -inf
        return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
    return solve(0, False)
```