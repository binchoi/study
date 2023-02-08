from typing import List


def solution(a, m, k):
    res = 0
    i = 0
    while i + m - 1 < len(a):
        found = two_sum(a, i, i+m-1, k)
        if found[0] != -1:
            res += min(found[0]-i+1, len(a) - i - m + 1)
            i = found[0] + 1
        else:
            i += 1
    return res


# not found => (-1,-1) / start & end are inclusive
def two_sum(a: List[int], start: int, end: int, target: int) -> (int, int):
    m = {}
    for i in range(start, end+1):
        if a[i] in m:
            return m[a[i]], i
        if target-a[i] not in m: # we take the first occuring pair - may not be necc
            m[target-a[i]] = i
    return (-1, -1)

# Not Optimal. O(N) possible

