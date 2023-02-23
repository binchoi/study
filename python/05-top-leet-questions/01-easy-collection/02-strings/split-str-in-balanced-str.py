
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = 0  # R - L
        for i in range(len(s)):
            count = count + 1 if s[i] == "R" else count - 1
            if count == 0:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.balancedStringSplit("RLRRLLRLRL"))
