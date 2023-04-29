from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # filter only useful words (e.g. XX, ab where ba exists)
        words_set = set(words)
        res = 0
        counter = Counter([w for w in words if w[0] == w[1] or w[::-1] in words_set])
        seen, lonely_palindrome_exists = set(), False
        for k, v in counter.items():
            if k not in seen:
                if k[0] != k[1]:
                    res += (min(v, counter[k[::-1]]) * 4)
                else:
                    pairs, rem = divmod(v, 2)
                    res += (4 * pairs)
                    if rem == 1:
                        lonely_palindrome_exists = True
                seen.add(k)
                seen.add(k[::-1])

        if lonely_palindrome_exists:
            res += 2

        return res

