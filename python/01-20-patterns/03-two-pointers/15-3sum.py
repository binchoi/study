from dataclasses import dataclass
from typing import List
import unittest


# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: List[List[int]]

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums=[-1, 0, 1, 2, -1, -4]),
                expect=[[-1, -1, 2], [-1, 0, 1]]
            ),
            TestCase(
                name="test 2",
                input=Args(nums=[0, 1, 1]),
                expect=[]
            ),
            TestCase(
                name="test 3",
                input=Args(nums=[0, 0, 0]),
                expect=[[0, 0, 0]]
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.threeSum(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
