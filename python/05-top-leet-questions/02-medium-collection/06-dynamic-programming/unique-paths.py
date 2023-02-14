from typing import List, Optional


# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
# or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
# bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Use SRTBOT:
# Sub-problem: unique paths from any other square to bottom-right
# Relate the sub-problems: total unique paths= unique paths from right square + unique paths from bottom square
# Topological Ordering: Top -> right, bottom -> right, bottom of each...
# Base: bottom right = 1
# Original: top left
# Time Complexity: T(n, m) = m * n (O(1)) = O(m*n)

class Solution:
    # DP (i.e. recursion with memo)
    # Time Complexity: O(n!)
    # Space Complexity: O(1) (excluding return data)
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None] * n for _ in range(m)]  # m x n
        memo[m - 1][n - 1] = 1  # base case
        return self.uniquePathsHelper(0, 0, memo)

    def uniquePathsHelper(self, x: int, y: int, memo: List[List[Optional[int]]]) -> int:
        if y >= len(memo) or x >= len(memo[0]):
            return 0

        if memo[y][x]:
            return memo[y][x]

        res = self.uniquePathsHelper(x, y + 1, memo) + self.uniquePathsHelper(x + 1, y, memo)
        memo[y][x] = res
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(m=3, n=7))
    print(sol.uniquePaths(m=3, n=2))
    print(sol.uniquePaths(m=1, n=1))
