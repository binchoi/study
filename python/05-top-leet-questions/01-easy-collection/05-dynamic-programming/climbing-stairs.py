
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # Memoization
    # Time Complexity: O(n)
    # Space Complexity: O(n) [+ O(n) call stack]
    memo = {1: 1, 2: 2}

    def climbStairsMemo(self, n: int) -> int:
        res = self.memo.get(n)
        if res:
            return res
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = res
        return res

    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for i in range(2, n):
            temp_b = b
            b = a + b
            a = temp_b

        return b

    def climbStairsSWusingWhile(self, n: int) -> int:
        # base-case
        if n == 1:
            return 1
        if n == 2:
            return 2

        n -= 2
        a, b = 1, 2
        while n > 0:
            t_b = b
            b = a+b
            a = t_b
            n -= 1
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairsMemo(5))
    print(sol.climbStairs(9))
