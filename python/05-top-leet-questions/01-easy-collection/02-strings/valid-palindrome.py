from collections import Counter
from typing import List

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
# and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        filtered_str = str.lower("".join(filter(str.isalnum, s)))
        left, right = 0, len(filtered_str) - 1
        while left < right:
            if filtered_str[left] != filtered_str[right]:
                return False
            left += 1
            right -= 1
        return True

    # note: could also implement in-place by traversing and skipping non-alphanumeric characters


if __name__ == "__main__":
    sol = Solution()
    s_arg = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s_arg))
