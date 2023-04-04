# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# BIT OPERATIONS CHEATSHEET (https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-
# bit-manipulation-to-solve-problems-easily-and-efficiently/?orderBy=most_votes)
# Set union                             A | B
# Set intersection                      A & B
# Set subtraction                       A & ~B
# Set negation                          ALL_BITS ^ A or ~A
# Set bit                               A |= 1 << bit
# Clear bit                             A &= ~(1 << bit)
# Test bit                              (A & 1 << bit) != 0
# Extract last bit                      A&-A or A&~(A-1) or x^(x&(x-1))
# Remove last bit                       A&(A-1)
# Get all 1-bits                        ~0

# Remove last bit (e.g.)
# 0100 -> 0100 & 0011 => 0000
# 0011 -> 0011 & 0010 => 0010 -> 0010 & 0001 => 0000
# 01010100 -> 01010100 & 01010011 => 01010000

class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def getSum(self, a: int, b: int) -> int:
        # let b contain the carry information
        if b == 0:
            return a
        return self.getSum(a ^ b, (a & b) << 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(3, 5))
    print(sol.getSum(31, -1))
    print(sol.getSum(48, 429))
