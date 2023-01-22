from dataclasses import dataclass
from typing import List
import unittest


# https://leetcode.com/problems/maximum-average-subarray-i/

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        max_sum = sum(nums[:k])
        shifting_sum = max_sum
        for i in range(k, len(nums)):
            shifting_sum -= nums[i-k]
            shifting_sum += nums[i]
            max_sum = max(max_sum, shifting_sum)
        return max_sum/k


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: float

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums=[1, 12, -5, -6, 50, 3], k=4),
                expect=12.75000
            ),
            TestCase(
                name="test 2",
                input=Args(nums=[5], k=1),
                expect=5.00000
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.findMaxAverage(nums=c.input.nums, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
