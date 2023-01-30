import random
from typing import List


# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the Solution class:

class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.min_stk.append(
            min(self.min_stk[-1], val) if len(self.min_stk) > 0 else val
        )

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


if __name__ == "__main__":
    sol = MinStack()
    for i in range(10, -1, -1):
        sol.push(i)
    print(sol.top())
    print(sol.getMin())

    sol.pop()
    print(sol.top())
    print(sol.getMin())
