import re
from dataclasses import dataclass
from typing import List, Set
import unittest


# https://leetcode.com/problems/contains-duplicate-ii/

# Given a string s and an integer k, return the length of the longest substring of s such that the
# frequency of each character in this substring is greater than or equal to k.


# TODO: try iterative solution (to prevent stack overflow) -- create guide
class Solution:
    # Time Complexity:  O(n log n)
    # Space Complexity: O(n^2)
    def longestSubstring(self, s: str, k: int) -> int:
        # base case # 1
        if len(s) < k:
            return 0

        # identify chars in s that do not occur k times or more - these cannot be included in the res substring
        bad_char_set = self._get_bad_char_set(s, k)
        if len(bad_char_set) == 0:  # base case # 2
            return len(s)

        # divide
        smaller_args = self._regex_split_string(s, bad_char_set)

        # conquer
        res = 0
        for cand_s in smaller_args:
            cand = self.longestSubstring(cand_s, k)
            # combine
            res = max(cand, res)

        return res

    def _get_bad_char_set(self, s: str, k: int) -> Set[str]:
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        res = set()
        for key, val in freq_map.items():
            if val < k:
                res.add(key)
        return res

    def _regex_split_string(self, s: str, bad_char_set: set) -> List[str]:
        regex_str = "|".join(bad_char_set)
        # print(f"given bad_chars={bad_char_set}, regex={regex_str}")
        return re.split(regex_str, s)


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="aaabb", k=3),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(s="ababbc", k=2),
                expect=5
            ),
            TestCase(
                name="custom test 1",
                input=Args(s="aaaadaaaaaaaaxaaacdccccc", k=2),
                expect=8
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.longestSubstring(s=c.input.s, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
