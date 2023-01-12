from dataclasses import dataclass
from typing import List, Optional
import unittest


# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort nums
        nums.sort()

        # set left and right pointer
        left, right = 0, len(nums)-1
        if nums[left] + nums[right] > 0:
            self.scanAscending(nums, left, right)

        return res

    def scanAscending(self, sorted_nums: List[int], left: int, right: int) -> Optional[List[int]]:
        middle = left + 1
        while middle < right:
            total = sorted_nums[left] + sorted_nums[middle] + sorted_nums[right]
            if total > 0:
                return None
            if total == 0:
                return [sorted_nums[left], sorted_nums[middle], sorted_nums[right]]
            middle += 1
        return None

    def scanDescending(self, sorted_nums: List[int], left: int, right: int) -> Optional[List[int]]:
        middle = right - 1
        while left < middle:
            total = sorted_nums[left] + sorted_nums[middle] + sorted_nums[right]
            if total < 0:
                return None
            if total == 0:
                return [sorted_nums[left], sorted_nums[middle], sorted_nums[right]]
            middle -= 1
        return None


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
