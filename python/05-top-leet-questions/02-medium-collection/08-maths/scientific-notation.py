import math

# Given integer and significant figures, return scientific notation of given integer

# Input / Output
# 12345, 2 -> 1.2   * 10^4
# 1, 1     -> 1     * 10^0
# 10, 3    -> 1.00  * 10^1
# 9999, 2  -> 1.0   * 10^4
# 0, 4     -> 0.000 * 10^0   # trailing zeros (if sf > len(num))


class Solution:

    # Time Complexity: O(n) where n = sf
    # Space Complexity: O(1)
    def get_scientific_notation(self, num: int, sf: int):
        sign = num / abs(num)
        num = num * sign

        # round
        num_of_digits = int(math.log10(num)) + 1  # represents the number of digits
        num = int(round(num, sf - num_of_digits))

        exp = int(math.log10(num))

        num_str = str(num)

        res = f"{'-' if sign<0 else ''}{num_str[0]}"
        if sf > 1:
            res += f".{num_str[1:sf]}"
        extra = sf - exp - 1
        if extra:
            res += ("0" * extra)
        res += f"*10^{exp}"
        print(res)


if __name__ == "__main__":
    sol = Solution()
    sol.get_scientific_notation(12345, 2)
    sol.get_scientific_notation(12345, 3)
    sol.get_scientific_notation(12345, 4)  # banker's rounding in action
    sol.get_scientific_notation(99999, 1)
    sol.get_scientific_notation(1, 5)
    sol.get_scientific_notation(2, 5)
    sol.get_scientific_notation(2341, 5)
    sol.get_scientific_notation(-1, 5)
    sol.get_scientific_notation(-9999, 2)

