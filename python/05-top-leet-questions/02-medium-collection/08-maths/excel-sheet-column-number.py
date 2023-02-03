from typing import List, Tuple

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its
# corresponding column number.

# For example
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


class Solution:
    # Time Complexity: O(n) where n = len(strs)
    # Space Complexity: O(1)
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        digit_val = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            res += self.alphabetToNumber(columnTitle[i]) * digit_val
            digit_val *= 26
        return res

    def titleToNumberAscending(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = 26*res + self.alphabetToNumber(columnTitle[i])
        return res

    def alphabetToNumber(self, c: str) -> int:
        # A -> 1, Z -> 26
        return ord(c) - ord('A') + 1


if __name__ == "__main__":
    sol = Solution()
    strs = ["AB", "ZY"]
    for s in strs:
        print(sol.titleToNumber(s))
        print(sol.titleToNumberAscending(s))
