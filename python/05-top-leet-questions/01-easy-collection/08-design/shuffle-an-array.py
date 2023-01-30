import random
from typing import List


# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array
# should be equally likely as a result of the shuffling.

# Implement the Solution class:

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return random.sample(self.nums, len(self.nums))


if __name__ == "__main__":
    sol = Solution([1, 2, 3, 4, 5])
    print(sol.reset())
    print(sol.shuffle())
    print(sol.reset())
