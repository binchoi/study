from collections import Counter
from typing import List, Dict


# Given a string array words, return an array of all characters that show up in all strings within the words
# (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq_dicts = []
        for w in words:
            freq_dicts.append(Counter(w))

        res = []
        for c in set(words[0]):
            count = min(f_dict.get(c, 0) for f_dict in freq_dicts)
            res += [c] * count
        return res


if __name__ == "__main__":
    sol = Solution()
    words = ["bella", "label", "roller"]
    print(sol.commonChars(words))

