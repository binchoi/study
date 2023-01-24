from collections import deque
from typing import List


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


def bitwise_operators_primer():
    # process: int -> binary -> operation -> decimal
    res = 10 & 4  # 1010 & 0100 -> 0000 = 2 + 4 + 8 = 0
    res = 10 | 4  # 1010 | 0100 -> 1110 = 2 + 4 + 8 = 14
    res = 10 ^ 4  # 1010 ^ 0100 -> 1110 = 2 + 4 + 8 = 14
    res = ~10     # ~1010 [1's complement] -> 32 bit int so... ~(...0000 1010) = (...1111 0101) [bitwise negation
                  # inverts the sign bit]. we have a negative number now which is represented using 2's complement
                  # -> (...0000 1011) = -11

    # note: 1’s complement of a binary number is another binary number obtained by toggling all bits in it.
    # note: 2’s complement of a binary number is 1, added to the 1’s complement of the binary number.

    # simple example for finding 2's complement (2's Complement of 100100):
    # Step 1: Traverse and let the bit stay the same until you find 1. Here yet.Answer = xxxx00
    # Step 2: You found 1. Let it stay the same.Answer = xxx100
    # Step 3: Flip all the bits left the 1. Answer = 011100.


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 3, 3, 5, 2, 2, 4]
    print(sol.singleNumber(nums))
