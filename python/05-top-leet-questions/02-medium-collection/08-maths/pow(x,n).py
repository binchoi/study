from typing import List, Tuple

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Constraints:
# * -100.0 < x < 100.0
# * -231 <= n <= 231-1
# * n is an integer.
# * -104 <= xn <= 104


class Solution:
    memo = {}

    # Time Complexity: O(log n) [b/c repeated division by 2 of n]
    # Space Complexity: O(log n)
    def myPow(self, x: float, n: int) -> float:
        if (x, n) in self.memo:
            return self.memo[(x, n)]
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x

        n_new, r = divmod(n, 2)
        res = self.myPow(x, n_new) * self.myPow(x, n_new + r)
        self.memo[(x, n)] = res
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def myPowNaive(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n > 0:
            res *= x
            n -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, -2))
    print(sol.myPow(2.00000, -39))
    print(sol.myPow(2.0023000, 9))
