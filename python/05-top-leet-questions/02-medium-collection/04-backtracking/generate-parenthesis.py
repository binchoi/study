from typing import List, Set


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution:
    # Backtracking
    # Time Complexity: O(2^n)
    # Space Complexity: O(n) excluding implicit recursive call stack
    def generateParenthesis(self, n: int) -> List[str]:
        res, cand = [], []
        self.generateParenthesisHelper(0, n, cand, res)
        return res

    def generateParenthesisHelper(self, net: int, n: int, cand: List[str], res: List[str]):
        if net < 0 or net > n or len(cand) > 2 * n:
            return
        if len(cand) == 2 * n and net == 0:
            res.append("".join(cand))
            return

        cand.append("(")
        self.generateParenthesisHelper(net + 1, n, cand, res)
        cand.pop()

        cand.append(")")
        self.generateParenthesisHelper(net - 1, n, cand, res)
        cand.pop()


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(5))
