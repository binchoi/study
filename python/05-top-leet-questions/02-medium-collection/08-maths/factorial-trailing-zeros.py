
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
import math


class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        max_order = int(math.log(n, 5))
        res = 0
        for i in range(1, max_order + 1):  # only log_5 n iterations
            res += n // (5 ** i)

        return res

    # Time Complexity: O(log_5 n)
    # Space Complexity: O(1)
    def trailingZeroesLogImplicit(self, n: int) -> int:
        res = 0
        order = 1
        div = n
        while div > 0:
            div, mod = divmod(n, 5 ** order)
            res += div
            order += 1

        return res

    # Recursive
    # Time Complexity: O(log_5 n)
    # Space Complexity: O(1) [excluding call stack]
    def trailingZeroesRecursive(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroesRecursive(n//5)

    # Time Complexity: O(n) [?]
    # Space Complexity: O(1)
    def trailingZeroesLinear(self, n: int) -> int:
        # count number of 5 factors
        res = 0
        for i in range(1, n+1):
            i, remainder = divmod(i, 5)
            while remainder == 0:
                res += 1
                i, remainder = divmod(i, 5)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))
    print(sol.trailingZeroes(31))
    print(sol.trailingZeroes(48))
    print(sol.trailingZeroesLogImplicit(3))
    print(sol.trailingZeroesLogImplicit(31))
    print(sol.trailingZeroesLogImplicit(48))
    print(sol.trailingZeroesLinear(3))
    print(sol.trailingZeroesLinear(31))
    print(sol.trailingZeroesLinear(48))

