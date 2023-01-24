from collections import Counter
from typing import List

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
# all the original letters exactly once.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# python handles unicode characters the same way it handles any other character (no adaption required)
#   if it was Go, we would not be able to parse the string to an array of bytes and instead use []runes instead


class Solution:
    # Time Complexity: O(n+m)
    # Space Complexity: O(n+m)
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq, t_freq = Counter(s), Counter(t)

        if len(s_freq) != len(t_freq):
            return False

        for k, v in s_freq.items():
            if t_freq[k] != v:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    s_arg = "anagram"
    t_arg = "nagaram"
    print(sol.isAnagram(s_arg, t_arg))

    s_arg = "anagram⾺"
    t_arg = "nag⾺aram"
    print(sol.isAnagram(s_arg, t_arg))


