from dataclasses import dataclass
from typing import List
import unittest

# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    # HASHMAP SOLUTION
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def containsNearbyDuplicateA(self, nums: List[int], k: int) -> bool:
        val_to_idx = {}
        for i, n in enumerate(nums):
            if n in val_to_idx and i-val_to_idx.get(n) <= k:
                return True
            val_to_idx[n] = i
        return False

    # SLIDING WINDOW SOLUTION
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def containsNearbyDuplicateB(self, nums: List[int], k: int) -> bool:
        window = set(nums[:k+1])
        if len(window) < k+1:
            return True
        for i in range(len(nums)-(k+1)):
            window.remove(nums[i])
            window.add(nums[i+k+1])
            if len(window) < k+1:
                return True
        return False

    # SLIDING WINDOW SOLUTION 2
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def containsNearbyDuplicateC(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if i > k:
                s.remove(nums[i-k-1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


class TestSolution(unittest.TestCase):
    def test_containsNearbyDuplicateA(self):
        @dataclass
        class Args:
            nums: List[int]
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: bool

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums=[1, 2, 3, 1], k=3),
                expect=True
            ),
            TestCase(
                name="test 2",
                input=Args(nums=[1, 0, 1, 1], k=1),
                expect=True
            ),
            TestCase(
                name="test 3",
                input=Args(nums=[1, 2, 3, 1, 2, 3], k=2),
                expect=False
            )
        ]

        for c in cases:
            solution = Solution()
            actual = solution.containsNearbyDuplicateA(nums=c.input.nums, k=c.input.k)
            self.assertEqual(
                c.expect,
                actual,
                f"Test {c.name} failed"
            )

    def test_containsNearbyDuplicateB(self):
        @dataclass
        class Args:
            nums: List[int]
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: bool

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums=[1, 2, 3, 1], k=3),
                expect=True
            ),
            TestCase(
                name="test 2",
                input=Args(nums=[1, 0, 1, 1], k=1),
                expect=True
            ),
            TestCase(
                name="test 3",
                input=Args(nums=[1, 2, 3, 1, 2, 3], k=2),
                expect=False
            )
        ]

        for c in cases:
            solution = Solution()
            actual = solution.containsNearbyDuplicateB(nums=c.input.nums, k=c.input.k)
            self.assertEqual(
                c.expect,
                actual,
                f"Test {c.name} failed"
            )

    def test_containsNearbyDuplicateC(self):
        @dataclass
        class Args:
            nums: List[int]
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: bool

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums=[1, 2, 3, 1], k=3),
                expect=True
            ),
            TestCase(
                name="test 2",
                input=Args(nums=[1, 0, 1, 1], k=1),
                expect=True
            ),
            TestCase(
                name="test 3",
                input=Args(nums=[1, 2, 3, 1, 2, 3], k=2),
                expect=False
            )
        ]

        for c in cases:
            solution = Solution()
            actual = solution.containsNearbyDuplicateC(nums=c.input.nums, k=c.input.k)
            self.assertEqual(
                c.expect,
                actual,
                f"Test {c.name} failed"
            )

if __name__ == '__main__':
    unittest.main()
