from dataclasses import dataclass
import unittest


# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string
# that meet the following conditions:
#   It has a length of k.
#   It is a divisor of num.

# Given integers num and k, return the k-beauty of num.

# Note:
#   Leading zeros are allowed.
#   0 is not a divisor of any value.

# A substring is a contiguous sequence of characters in a string.


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        num_str = str(num)
        for i in range(0, len(num_str) - k + 1):
            n = int(num_str[i:i+k])
            if n != 0 and num % n == 0:
                res += 1
        return res


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            num: int
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(num=240, k=2),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(num=430043, k=2),
                expect=2
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.divisorSubstrings(num=c.input.num, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
