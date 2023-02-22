from typing import Tuple
from math import comb
from collections import Counter

# Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j],
# where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

import math
from typing import List
from collections import Counter


def solution(a: List[int]) -> int:
    res = 0
    len_counter = Counter([int(math.log10(val))+1 for val in a])
    for a_i in a:
        for k, v in len_counter.items():
            res += (v * a_i * (10 ** k)) # when it's chosen first
        res += (a_i * len(a))
    return res

