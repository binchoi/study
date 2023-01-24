from typing import List

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to
# C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:
# - Read in and ignore any leading whitespace.
# - Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if
#   it is either. This determines if the final result is negative or positive respectively. Assume the result is
#   positive if neither is present.
# - Read in next the characters until the next non-digit character or the end of the input is reached. The rest of
#   the string is ignored.
# - Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer
#   is 0. Change the sign as necessary (from step 2).
# - If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it
#   remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater
#   than 231 - 1 should be clamped to 231 - 1.
# - Return the integer as the final result.

# Note:
# - Only the space character ' ' is considered a whitespace character.
# - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# ***
# Let's try to implement this using Deterministic Finite Automata (DFA) where states are based on what your prev char
# was.


class Solution:
    # state = 0 -> prev: start / ' '
    # state = 1 -> prev: + / -
    # state = 2 -> prev: digit

    INT32_MAX = 2 ** 31 - 1
    INT32_MIN = -(2 ** 31)

    def myAtoi(self, s: str) -> int:
        state = 0  # DFA
        pos, res, sign = 0, 0, 1

        # base case
        if len(s) == 0:
            return 0

        while pos < len(s):
            if state == 0:
                if s[pos] == " ":
                    state = 0
                elif s[pos] in {"-", "+"}:  # set literal
                    if s[pos] == "-":
                        sign = -1
                    state = 1
                elif str.isdigit(s[pos]):
                    res = 10 * res + int(s[pos])
                    state = 2
                else:
                    return 0

            elif state == 1:
                if str.isdigit(s[pos]):
                    res = 10 * res + int(s[pos])
                    state = 2
                else:
                    return 0

            elif state == 2:
                if str.isdigit(s[pos]):
                    if sign == -1:
                        res_threshold = abs(self.INT32_MIN) // 10
                        if res < res_threshold or (res == res_threshold and int(s[pos]) <= abs(self.INT32_MIN) % 10):
                            res = res * 10 + int(s[pos])
                        else:
                            return self.INT32_MIN
                    else:
                        res_threshold = self.INT32_MAX // 10
                        if res < res_threshold or (res == res_threshold and int(s[pos]) <= self.INT32_MAX % 10):
                            res = res * 10 + int(s[pos])
                        else:
                            return self.INT32_MAX
                else:
                    break

            else:
                raise Exception("Uh oh! Something seems off!")

            # increment
            pos += 1

        return sign * res

    def myAtoiNaive(self, s: str) -> int:
        try:
            pointer = Pointer(s)
            # step 1
            while s[pointer.val] == " ":
                pointer.increment()

            # step 2
            sign = 1
            if s[pointer.val] in set(("-", "+")):
                if s[pointer.val] == "-":
                    sign = -1
                pointer.increment()

            # step 3-1
            while s[pointer.val] == "0":  # skip leading 0s
                pointer.increment()
        except:
            return 0

        # step 3
        abs_val_as_str = ""
        try:
            while str.isdigit(s[pointer.val]):
                abs_val_as_str += s[pointer.val]
                pointer.increment()
        except:
            pass

        abs_val = int(abs_val_as_str) if abs_val_as_str != "" else 0

        if sign == -1:
            return -1 * abs_val if abs_val <= 2 ** 31 else -(2 ** 31)
        return abs_val if abs_val <= 2 ** 31 - 1 else 2 ** 31 - 1


class Pointer:
    def __init__(self, s: str):
        self.cap = len(s)
        self.val = 0

        if self.cap == 0:
            raise Exception("Empty string")

    def increment(self):
        self.val += 1
        if self.val >= self.cap:
            raise Exception("Cap exceeded")


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("            -000001234"))
