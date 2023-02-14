from typing import Tuple
from math import comb
from collections import Counter

# Given an array of integers a, your task is to count the number of pairs i and j (where 0 ≤ i < j < a.length),
# such that a[i] and a[j] are digit anagrams.


def solution(a):
    # create counter for each string, then count freq
    for i, n in enumerate(a):
        a[i] = int_to_digit_arr(n)  # a: List[List[int]]

    anagram_freq = Counter(a)

    res = 0
    for v in anagram_freq.values():
        if v > 1:
            res += comb(v, 2)
    return res


def int_to_digit_arr(num: int) -> Tuple[int]:
    res = [0] * 10
    for d in str(num):
        res[ord(d) - ord("0")] += 1
    return tuple(res)

