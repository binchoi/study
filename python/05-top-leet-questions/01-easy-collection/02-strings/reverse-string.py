from typing import List

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(s)
    sol.reverseString(s)
    print(s)
