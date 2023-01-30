import math

from typing import List

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
# ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of calls to the API.


class Solution:
    # Binary Search
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            if self.checkIsBadVersion(mid):
                if not self.checkIsBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1

    def checkIsBadVersion(self, k: int):
        if k < 1:
            return False
        res = self.isBadVersion(k)
        return res

    # Binary Search + Memoization
    # Time Complexity: O(log(n))
    # Space Complexity: O(n)
    def firstBadVersionMemoized(self, n: int) -> int:
        low, high = 1, n
        memo = [None] * (n + 1)

        while low <= high:
            mid = (low + high) // 2
            if self.memoIsBadVersion(mid, memo):
                if not self.memoIsBadVersion(mid - 1, memo):  # first bad version's prev returns false
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1

    def memoIsBadVersion(self, k: int, memo):
        if k < 1:
            return False
        if memo[k]:
            return memo[k]
        res = self.isBadVersion(k)
        memo[k] = res
        return res

    def isBadVersion(self, k: int):
        if k < 8:  # 8 is first bad version
            return False
        return True

    # Alternative Clean Binary Search Implementation
    def firstBadVersionAlt(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high-low) // 2
            if self.isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    sol = Solution()
    # both returns 8 as expected
    print(sol.firstBadVersion(10))
    print(sol.firstBadVersionMemoized(27))
    print(sol.firstBadVersionAlt(40))
