from collections import deque
from typing import List


# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
# the integer. The digits are ordered from most significant to least significant in left-to-right order. The
# large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        while pointer >= 0:
            digits[pointer] = (digits[pointer] + 1) % 10
            if digits[pointer] != 0:
                break
            pointer -= 1
        if pointer == -1:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    sol = Solution()
    nums = [9, 9, 8, 9, 9]
    print(sol.plusOne(nums))
