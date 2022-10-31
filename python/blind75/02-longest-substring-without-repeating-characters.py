import dataclasses
from typing import Any

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # brute force
    def lengthOfLongestSubstringBF(self, s: str) -> int:
        s_len = len(s)
        best_so_far = 0
        for i in range(s_len):
            cnt = 1
            seen_so_far = set(s[i])  # init set with character on current index
            for j in range(i+1, s_len):
                if s[j] in seen_so_far:
                    best_so_far = max(best_so_far, cnt)
                    break
                else:
                    cnt += 1
                    seen_so_far.add(s[j])
                    if j == s_len:
                        best_so_far = max(best_so_far, cnt)
        return best_so_far

    # sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 0

# Test
@dataclasses.dataclass
class Testcase:
    name: str
    given: Any
    expect: Any


if __name__ == '__main__':
    mySol = Solution()

    cases = [
        Testcase(
            name="empty string",
            given="",
            expect=0,
        ),
        Testcase(
            name="test string 1",
            given="abcabcbb",
            expect=3,
        ),
        Testcase(
            name="test string 2",
            given="bbbbb",
            expect=1,
        ),
        Testcase(
            name="test string 3",
            given="pwwkew",
            expect=3,
        ),
    ]

    for c in cases:
        evaluated_value = mySol.lengthOfLongestSubstringBF(c.given)
        assert c.expect == evaluated_value

