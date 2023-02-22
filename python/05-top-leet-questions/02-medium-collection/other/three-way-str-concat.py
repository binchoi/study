from typing import Tuple
from math import comb
from collections import Counter

# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b
# and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

from typing import Set, List


# output: number of possibilities of non-empty a, b, c:  a + b != b + c != c + a
def solution(s: str) -> int:
    # pos = 0
    abc = []  # will contain a, b, c
    res = [0]
    backtrack(s, abc, res)  # len(abc) = 0 at first
    return res[0]


def backtrack(s: str, abc: List[str], res: List[int]):
    # print(f"backtrack given {s}, {abc}, {res}")
    if len(abc) == 2:  # catch at 2
        if len({abc[0] + abc[1], abc[1] + s, s + abc[0]}) == 3:
            res[0] += 1
    else:  # 0, 1
        for i in range(1, len(s)):
            cand = s[:i]
            # print(f"adding {cand} to {abc}")
            abc.append(cand)
            backtrack(s[i:], abc, res)
            abc.pop()





