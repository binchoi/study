from typing import List

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.


class Solution:
    # Time Complexity: O(n-m)
    # Space Complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for i in range(len(haystack)-needle_len+1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("            -000001234", "1234"))
