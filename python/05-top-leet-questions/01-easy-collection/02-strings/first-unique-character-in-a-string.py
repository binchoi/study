from collections import OrderedDict

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_uniq_set = set()
        cand_map = OrderedDict()  # dict that keeps order
        for i, c in enumerate(s):
            if c not in non_uniq_set:
                if c not in cand_map:
                    cand_map[c] = i
                else:
                    del cand_map[c]
                    non_uniq_set.add(c)

        return cand_map.popitem(last=False)[1] if len(cand_map) > 0 else -1  # last = False (FIFO) / True (LIFO)

    def firstUniqCharNative(self, s: str) -> int:
        cand_map = OrderedDict()
        for i, c in enumerate(s):
            if c in cand_map:
                cand_map[c] = (cand_map[c][0]+1, cand_map[c][1])
            else:
                cand_map[c] = (1, i)

        for k, v in cand_map.items():
            if v[0] == 1:
                return v[1]
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqCharNative("leetcode"))
