from dataclasses import dataclass
import unittest

# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.
from typing import Dict


# Time Complexity:  O(n)
# Space Complexity: O(n) / O(1) [<- countGoodSubstringsSimple]
class Solution:
    def __init__(self):
        self._histogram: Dict[str, int] = {}

    def add_char(self, c):
        self._histogram[c] = self._histogram.get(c, 0) + 1

    def remove_char(self, c):
        new_count = self._histogram.get(c) - 1
        if new_count == 0:
            self._histogram.pop(c)
        else:
            self._histogram[c] = new_count

    def is_good(self, window_size):
        return len(self._histogram) == window_size

    def countGoodSubstrings(self, s: str) -> int:
        window_size = 3
        # init window
        if len(s) < window_size:
            return 0
        for i in range(window_size):
            self.add_char(s[i])
        res = 1 if self.is_good(window_size) else 0

        for i in range(window_size, len(s)):
            # shift window
            self.remove_char(s[i-window_size])
            self.add_char(s[i])
            if self.is_good(window_size):
                res += 1
        return res

    def countGoodSubstringsSimple(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)-1):  # range doesn't throw exception if end is before beginning (it just doesn't run)
            if s[i-1] != s[i] and s[i] != s[i+1] and s[i-1] != s[i+1]:
                res += 1
        return res

# countGoodSubstringsSimple is a wonderful solution as it demonstrates that SLIDING WINDOW questions do not
# require an additional data structure that holds the entire data of the window. Like above, it could utilize
# the provided data structure (e.g. s above) and simply use one POINTER to mark the beginning, middle, or end
# of the window! In the above example we chose to use a pointer to represent the center of the window.


class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="xyzzaz"),
                expect=1
            ),
            TestCase(
                name="test 2",
                input=Args(s="aababcabc"),
                expect=4
            ),
        ]

        for c in cases:
            solution = Solution()

            actual = solution.countGoodSubstrings(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )

    def test_solution_simple(self):
        @dataclass
        class Args:
            s: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="xyzzaz"),
                expect=1
            ),
            TestCase(
                name="test 2",
                input=Args(s="aababcabc"),
                expect=4
            ),
        ]

        for c in cases:
            solution = Solution()

            actual = solution.countGoodSubstringsSimple(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )

if __name__ == '__main__':
    unittest.main()
