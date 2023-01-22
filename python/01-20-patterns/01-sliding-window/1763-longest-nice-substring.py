from dataclasses import dataclass
from typing import List, Set, Iterator
import unittest


# https://leetcode.com/problems/longest-nice-substring/

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
# appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of
# the earliest occurrence. If there are none, return an empty string.


class Solution:
    # Time Complexity:  O(n log n) where the base of log is not necessarily 2 (?)
    # Space Complexity: O(n^2) [consider if divider is always in the middle of the string (n -> n-1 -> n-3 ... 1)]
    def longestNiceSubstring(self, s: str) -> str:
        # base cases
        if len(s) < 2:
            return ""

        lonely_alphabets_set = self._find_lonely_alphabets(s)
        if len(lonely_alphabets_set) == 0:
            return s

        # divide
        smaller_str_arr = self._splice_string(s, lonely_alphabets_set)

        res = ""
        for s in smaller_str_arr:
            # conquer
            v = self.longestNiceSubstring(s)
            # combine
            if len(v) > len(res):
                res = v

        return res

    def _find_lonely_alphabets(self, s: str) -> Set[str]:
        search = set(s)
        res = set(s)
        for c in search:
            if c.upper() in search and c.lower() in search:
                res.discard(c.upper())
                res.discard(c.lower())
        return res

    def _splice_string(self, s: str, blacklist_alphabets: set) -> List[str]:
        locs = [i for i, c in enumerate(s) if c in blacklist_alphabets]

        res = []
        start = 0
        for i in locs:
            if start < i:
                res.append(s[start:i])
            start = i+1

        if start < len(s)-1:
            res.append(s[start:])

        return res


class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: str

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="YazaAay"),
                expect="aAa"
            ),
            TestCase(
                name="test 2",
                input=Args(s="Bb"),
                expect="Bb"
            ),
            TestCase(
                name="test 3",
                input=Args(s="c"),
                expect=""
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.longestNiceSubstring(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
