from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution:
    # Time Complexity: O(nx) where n is length of shortest string in strs & x is the number of string items in strs
    # Space Complexity: O(x)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            ith_chars = {s[i] for s in strs}
            if len(ith_chars) != 1:
                return res
            res += ith_chars.pop()
        return res


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))
