from typing import Tuple
from math import comb
from collections import Counter

# A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. In other words,
# each element is either strictly greater than its neighbouring elements or strictly less than its neighbouring
# elements.

def solution(a):
    # traverse from left to right while keeping min distance to building (from left)
    # traverse from right to left while keeping min distance to building (from right) -> min(with above)
    # e.g. [{gym: 1, school:2, store:0}, {gym: 1, school:2, store:0}, {gym: 1, school:2, store:0}]

    a = []
    req = {'dsf'}
    a.sort(key=lambda d: sum(v for k, v in d.items() if k in req))
    return a[0]

