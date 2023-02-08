import math

# Given integer and significant figures, return scientific notation of given integer

# Input / Output
# 12345, 2 -> 1.2   * 10^4
# 1, 1     -> 1     * 10^0
# 10, 3    -> 1.00  * 10^1
# 9999, 2  -> 1.0   * 10^4
# 0, 4     -> 0.000 * 10^0   # trailing zeros (if sf > len(num))


class Solution:

    # Time Complexity: O()
    # Space Complexity: O()
    def get_scientific_notation(self, num: int, sf: int):
        exp = int(math.log10(num))
        pass


if __name__ == "__main__":
    sol = Solution()
    sol.get_scientific_notation(12345, 2)
    sol.get_scientific_notation(12345, 20)
    # print(sol.get_scientific_notation(2.00000, -39))
    # print(sol.get_scientific_notation(2.0023000, 9))
