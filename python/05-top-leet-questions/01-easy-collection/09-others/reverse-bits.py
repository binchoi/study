
# Reverse bits of a given 32 bits unsigned integer.


class Solution:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31):
            res += n%2
            n = n >> 1
            res = res << 1
        res += n%2
        return res


if __name__ == "__main__":
    sol = Solution()
    # both returns 8 as expected
    print(sol.reverseBits(1234))
    print(sol.reverseBits(12))
    print(sol.reverseBits(123234))
