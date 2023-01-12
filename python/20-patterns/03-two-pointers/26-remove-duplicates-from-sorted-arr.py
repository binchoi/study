from dataclasses import dataclass
from typing import List
import unittest

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
# each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have
# the result be placed in the first part of the array nums. More formally, if there are k elements after
# removing the duplicates, then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place
# with O(1) extra memory.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
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
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [1,1,2]),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [0,0,1,1,1,2,2,3,3,4]),
                expect=5
            ),
        ]

        for c in cases:
            solution = Solution()

            actual = solution.removeDuplicates(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
