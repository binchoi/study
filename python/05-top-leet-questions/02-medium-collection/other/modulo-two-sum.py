from typing import List
from collections import defaultdict

# You are given an array of integers a and an integer k. Your task is to calculate the number of ways to
# pick two different indices i < j, such that a[i] + a[j] is divisible by k.


def solution(a: List[int], k: int) -> int:
    m = defaultdict(int)
    res = 0
    for i in a:
        a_val = i % k
        res += m[a_val] if a_val > 0 else m[k]
        m[k - a_val] += 1
    return res


