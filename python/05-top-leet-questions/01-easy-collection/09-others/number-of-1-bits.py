
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as
# the Hamming weight).


class Solution:
    # Time Complexity: O(1) as while loop will execute at most 32 times (bounded by a constant)
    # Space Complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 2)  # if ODD, right most bit is 1
            n = n >> 1      # bit shift to the right by one
        return res


if __name__ == "__main__":
    sol = Solution()
    # both returns 8 as expected
    print(sol.hammingWeight(10))
    print(sol.hammingWeight(27))
    print(sol.hammingWeight(40))
