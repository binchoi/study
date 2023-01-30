import math

from typing import List

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

# Follow up: Could you solve it without loops/recursion?


class Solution:
    # Time Complexity: O(log_3(n))
    # Space Complexity: O(1)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            n, r = divmod(n, 3)
            if r != 0:
                return False
        return True

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isPowerOfThreeMath(self, n: int) -> bool:
        return math.log10(n) / math.log10(3) % 1 == 0

    # Since 3 is a prime, the only divisors of 3^19 are 3^0, 3^1, 3^2, 3^3, ... 3^18, 3^19.
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isPowerOfThreeMathTwo(self, n: int) -> bool:
        return 3**19 % n == 0


if __name__ == "__main__":
    sol = Solution()
    n = 15
    print(sol.isPowerOfThree(n))
    print(sol.isPowerOfThree(27))
    print(sol.isPowerOfThreeMath(27))
    print(sol.isPowerOfThreeMathTwo(27))
