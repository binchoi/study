from typing import Tuple
from math import comb
from collections import Counter

# https://www.youtube.com/watch?v=rw4s4M3hFfs&ab_channel=Cl%C3%A9mentMihailescu

blocks = [
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    },
    {
        "gym": True,
        "school": False,
        "store": False
    }
]

def solution(a):
    # traverse from left to right while keeping min distance to building (from left)
    # traverse from right to left while keeping min distance to building (from right) -> min(with above)
    # e.g. [{gym: 1, school:2, store:0}, {gym: 1, school:2, store:0}, {gym: 1, school:2, store:0}]

    a = []
    req = {'dsf'}
    a.sort(key=lambda d: sum(v for k, v in d.items() if k in req))
    return a[0]

