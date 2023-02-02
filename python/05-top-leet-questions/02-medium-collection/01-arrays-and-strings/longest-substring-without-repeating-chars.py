from typing import List, Tuple

# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    # Time Complexity: O(n) where n = len(s) [two pointers -> max 2n iterations]
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = j = 0  # start/end idx (inclusive, exclusive)
        res = 0
        seen = set()
        while i < len(s):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            i += 1
            res = max(res, i - j)
        return res

    # Optimized using Hashmap to store the idx of where the character was last found
    # Same Time and Space Complexity
    def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = j = 0  # start/end idx (inclusive, exclusive)
        res = 0
        seen = {}
        while i < len(s):
            if s[i] in seen:
                j = max(j, seen[s[i]] + 1)  # compute max so j is not moved backwards
            seen[s[i]] = i  # write or overwrite
            i += 1
            res = max(res, i-j)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
    print(sol.lengthOfLongestSubstringOptimized(s))
