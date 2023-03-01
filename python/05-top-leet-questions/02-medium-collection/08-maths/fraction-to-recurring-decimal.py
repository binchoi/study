
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.


class Solution:
    # Idea: recurring decimals are like linked lists with cycles. If we keep track of the remainder at each division
    # we can identify the presence of a cycle.
    # Time Complexity: O(denominator), the while-loop in fractionalDivision will terminate after d iterations max
    # Space Complexity: O(denominator - 1) [for denominator = d, there can be up to d-1 unique keys in hashmap memo
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = (numerator < 0) ^ (denominator < 0)

        div, mod = divmod(abs(numerator), abs(denominator))
        if mod == 0:
            return str(div) if not is_negative else str(-div)

        fractional_part = self.fractionalDivision(mod, abs(denominator))
        return f"{div}.{fractional_part}" if not is_negative else f"-{div}.{fractional_part}"

    # where num < dem
    def fractionalDivision(self, num: int, dem: int) -> str:
        memo = {}
        res = []
        while num != 0:
            if num in memo:
                res.insert(memo[num], "(")
                res.append(")")
                return "".join(res)

            memo[num] = len(res)
            div, num = divmod(num * 10, dem)
            res.append(str(div))
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(1, 7))
    print(sol.fractionToDecimal(1, 17))
    print(sol.fractionToDecimal(1, 19))


# random notes: Every rational number is either a terminating or repeating decimal
# A fraction in lowest terms with a prime denominator other than 2 or 5 (i.e. coprime to 10) always produces a
# repeating decimal. The length of the repetend (period of the repeating decimal segment) of 1/p is equal to the
# order of 10 modulo p. If 10 is a primitive root modulo p, then the repetend length is equal to p − 1; if not, then
# the repetend length is a factor of p − 1. This result can be deduced from Fermat's little theorem, which states
# that 10p−1 ≡ 1 (mod p).
