from typing import Tuple
from math import comb
from collections import Counter

# Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) such that
# i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.
#
# Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of 2.

from typing import List


def solution(numbers: List[int]) -> int:
    res = 0
    power, power_set = 1, set()
    while power <= 2 * max(numbers):
        power_set.add(power)
        power *= 2

    demand_dict = {}
    for i in range(len(numbers)):
        for p in power_set:
            if p - numbers[i] not in demand_dict:
                demand_dict[p - numbers[i]] = 0
            demand_dict[p - numbers[i]] += 1

        if numbers[i] in demand_dict:
            res += demand_dict[numbers[i]]

    return res


# todo: check https://codesignal.com/blog/interview-prep/example-codesignal-questions/
def solutionOptimal(numbers: List[int]) -> int:
    count = 0

    for i in range(31):
        key = 2 ** i

        my_map = {}
        for num in numbers:
            my_map[num] = my_map.get(num, 0) + 1
            to_find = key - num
            if to_find in my_map:
                count += 1

    return count