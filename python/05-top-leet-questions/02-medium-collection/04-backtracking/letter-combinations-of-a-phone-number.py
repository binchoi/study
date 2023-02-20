from typing import List, Optional


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
# could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map
# to any letters.


class Solution:

    DIGIT_TO_CHARS = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    # Backtracking (= DFS)
    # Time Complexity: O(4^n) where n = len(digits)
    # Space Complexity: O(n) (excluding call stack) to keep a buffer of maximum n items (for cand strings)
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        self.letterCombinationsHelper(digits, 0, "", res)
        return res

    def letterCombinationsHelper(self, digits: str, i: int, cand: str, res: List[str]):
        if i >= len(digits):
            res.append(cand)
            return
        for c in self.DIGIT_TO_CHARS[digits[i]]:
            self.letterCombinationsHelper(digits, i + 1, cand + c, res)  # use string builder instead

    def letterCombinationsSpaceOptimized(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        self.letterCombinationsHelperSpaceOptimized(digits, 0, [], res)
        return res

    def letterCombinationsHelperSpaceOptimized(self, digits: str, i: int, cand: List[str], res: List[str]):
        if i >= len(digits):
            res.append("".join(cand))
            return
        for c in self.DIGIT_TO_CHARS[digits[i]]:
            cand.append(c)
            self.letterCombinationsHelperSpaceOptimized(digits, i + 1, cand, res)
            cand.pop()

    # Time Complexity: O(4^n) where n = len(digits)
    # Space Complexity: O(4^n) [geometric series; 1 + 4 + 16 + ... = a(1-r^n)/(1-r)]
    def letterCombinationsHelperIterative(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res

        res.append("")
        while len(res[0]) < len(digits):
            tmp = []
            for s in res:
                for c in self.DIGIT_TO_CHARS[digits[len(res[0])]]:
                    tmp.append(s+c)
            res = tmp
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinationsSpaceOptimized("23"))
    print(sol.letterCombinationsHelperIterative("23"))
    print(sol.letterCombinations("485"))
    print(sol.letterCombinationsSpaceOptimized("485"))
    print(sol.letterCombinationsHelperIterative("485"))
    print(sol.letterCombinations("77"))
    print(sol.letterCombinationsSpaceOptimized("77"))
    print(sol.letterCombinationsHelperIterative("77"))

