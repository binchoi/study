from typing import List, Tuple

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

# Constraints
# * 1 <= strs.length <= 10^4
# * 0 <= strs[i].length <= 100
# * strs[i] consists of lowercase English letters.


class Solution:
    # Time Complexity: O(n) where n = len(strs) [convert_str_to_tup considered O(1) given that len(s) <= 100] or O(n*m)
    # Space Complexity: O(n) or O(n*m) if we consider the length of the individual strings to be significant
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            anagram_tup = self.convert_str_to_tup(s)
            if anagram_tup in anagram_map:
                anagram_map[anagram_tup].append(s)
            else:
                anagram_map[anagram_tup] = [s]
        return list(anagram_map.values())

    def convert_str_to_tup(self, s: str) -> Tuple[int]:
        res = [0] * 26
        for c in s:
            res[ord(c) - ord("a")] += 1
        return tuple(res)


if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(sol.groupAnagrams(strs))
