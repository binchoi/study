from typing import List

# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    # Time Complexity: O(n sqrt(n)) or O(n log(log n))
    # Space Complexity: O(1)
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [1] * n  # 0 ... n-1
        is_prime[0] = is_prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            is_prime[2*i: n: i] = [0] * len(is_prime[2*i: n: i])
        return sum(is_prime)

    # Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def countPrimesBF(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            cnt += self.isPrime(i)
        return cnt

    def isPrime(self, v: int) -> bool:
        for i in range(2, v // 2 + 1):
            if v % i == 0:
                return False
        return True

    # Failed Optimization
    prime_arr = None

    def countPrimesNaive(self, n: int) -> int:
        self.prime_arr = [None] * (n + 1)
        cnt = 0
        for i in range(2, n):
            cnt += self.isPrime(i)
        return cnt

    def isPrimeNaive(self, v: int) -> bool:
        self.color_multiples_false(v)

        if self.prime_arr[v]:
            return False

        for i in range(2, v // 2 + 1):
            if v % i == 0:
                return False
        return True

    def color_multiples_false(self, v: int) -> None:
        i = 2 * v
        while i < len(self.prime_arr):
            self.prime_arr[i] = False
            i += v


if __name__ == "__main__":
    sol = Solution()
    n = 150
    print(sol.countPrimes(n))
