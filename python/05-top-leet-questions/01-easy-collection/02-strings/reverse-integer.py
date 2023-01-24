from typing import List

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
# outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# NOTE: in python, strings are mutable (unlike in many other languages like Java). Hence, we do not require any
# special classes or tools (e.g. StringBuilder in Java) to prevent performance issues.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseNaive(self, x: int) -> int:
        res_str = ""
        for c in str(x)[::-1]:
            if c == "-":
                res_str = f"-{res_str}"
            else:
                res_str += c

        return int(res_str) if -(2**31) < int(res_str) < 2**31-1 else 0

    INT32_MIN = - 2 ** 31
    INT32_MAX = 2 ** 31 - 1

    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            tail_digit = x % 10
            if res > self.INT32_MAX // 10 or (res == self.INT32_MAX // 10 and tail_digit > 7):
                return 0
            if res < self.INT32_MIN // 10 or (res == self.INT32_MIN // 10 and tail_digit > 8):
                return 0
            x = x // 10
            res = 10*res + tail_digit
        return sign * res


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(1234))
