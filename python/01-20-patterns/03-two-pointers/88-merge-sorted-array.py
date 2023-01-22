from dataclasses import dataclass
from typing import List
import unittest


# https://leetcode.com/problems/contains-duplicate-ii/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums1: List[int]
            m: int
            nums2: List[int]
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: None

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3),  # TODO: write your test cases
                expect=None  # [1,2,2,3,5,6]
            ),
            TestCase(
                name="test 2",
                input=Args(nums1=[1], m=1, nums2=[], n=0),
                expect=None  # [1]
            ),
            TestCase(
                name="test 3",
                input=Args(nums1=[0], m=0, nums2=[1], n=1),
                expect=None  # [1]
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.merge(nums1 = c.input.nums1, m = c.input.m, nums2 = c.input.nums2, n = c.input.n)

            print(f"merged array {c.input.nums1}")

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
