from typing import List, Tuple

# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        lo, hi = 0, 0  # lo, hi
        for i in range(len(s)):
            o_lo, o_hi = self.longest_odd_palindrome(s, i)
            if hi - lo < o_hi - o_lo:
                lo, hi = o_lo, o_hi
            e_lo, e_hi = self.longest_even_palindrome(s, i)
            if hi - lo < e_hi - e_lo:
                lo, hi = e_lo, e_hi
        return s[lo:hi + 1]

    def longest_odd_palindrome(self, s: str, i: int):
        lo, hi = i - 1, i + 1
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1

    def longest_even_palindrome(self, s: str, i: int):
        lo, hi = i - 1, i
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1

    # can use one common helper function
    def longestPalindromeSimplified(self, s: str) -> str:
        lo, hi = 0, 0  # lo, hi
        for i in range(len(s)):
            o_lo, o_hi = self.expand_around_center(s, i, i)
            if hi - lo < o_hi - o_lo:
                lo, hi = o_lo, o_hi
            e_lo, e_hi = self.expand_around_center(s, i-1, i)
            if hi - lo < e_hi - e_lo:
                lo, hi = e_lo, e_hi
        return s[lo:hi + 1]

    def expand_around_center(self, s: str, lo: int, hi: int):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1


if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))
    print(sol.longestPalindromeSimplified(s))
