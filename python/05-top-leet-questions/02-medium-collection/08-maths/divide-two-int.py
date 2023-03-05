
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer 
# range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
# and if the quotient is strictly less than -231, then return -231.


# Constraints
# * -231 <= dividend, divisor <= 231 - 1
# * divisor != 0

# INPUT - OUTPUT
# IN:  8, 6
# OUT: 1

# counter = 0 -> 1
# 8 - 6   = 2 ... ..  2 - 6 < 0


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend - divisor >= 0:
            dividend -= divisor
            res += 1
        return -res if is_negative else res


if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(8, 6))
    print(sol.divide(112, 10))
    print(sol.divide(8, 1))
    print(sol.divide(0, 1))
    print(sol.divide(-8, 6))
    print(sol.divide(-112, 10))
    print(sol.divide(8, -1))
    print(sol.divide(0, -1))
