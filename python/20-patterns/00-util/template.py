from dataclasses import dataclass
from typing import List
import unittest

# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def someQuestion(self, nums: List[int], k: int) -> bool:
        pass


# Test
class TestSolution(unittest.TestCase):
    def mainTest(self):
        @dataclass
        class Args:  # TODO: change this
            nums: List[int]
            k: int

        @dataclass   # TODO: change this
        class TestCase:
            name: str
            input: Args
            expect: bool

        cases = [    # TODO: write your test cases
            TestCase(
                name="test 1",
                input=Args(nums=[1, 2, 3, 1], k=3),
                expect=True
            ),
            TestCase(
                name="test 1",
                input=Args(nums=[1, 0, 1, 1], k=1),
                expect=True
            ),
            TestCase(
                name="test 1",
                input=Args(nums=[1, 2, 3, 1, 2, 3], k=2),
                expect=False
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.someQuestion(nums=c.input.nums, k=c.input.k)  # TODO: change this

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )
