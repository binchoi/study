
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stk = []
        for c in s:
            if c not in parenthesis_map:
                stk.append(c)
            else:
                if not stk or stk[-1] != parenthesis_map[c]:
                    return False
                stk.pop()
        return len(stk) == 0


if __name__ == "__main__":
    sol = Solution()
    # both returns 8 as expected
    print(sol.isValid("(]"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("()"))
    print(sol.isValid("(((("))
