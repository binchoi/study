from typing import List
import numpy as np


# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
# according to the following rules:
# - Each row must contain the digits 1-9 without repetition.
# - Each column must contain the digits 1-9 without repetition.
# - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    # Time Complexity: O(n*m)
    # Space Complexity: O(n*m)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # by row
        for r in board:
            if not self.isValidSet(r):
                return False

        # by col
        for c in np.transpose(board):
            if not self.isValidSet(c):
                return False

        # by square
        corner_idx = [0, 3, 6]
        for i in corner_idx:
            for j in corner_idx:
                if not self.isValidSet(self.getSquareSet(i, j, board)):
                    return False
        return True

    def isValidSet(self, items: List[str]) -> bool:
        seen = set()
        for v in items:
            if v != ".":
                if v in seen:
                    return False
                else:
                    seen.add(v)
        return True

    def getSquareSet(self, x: int, y: int, board: List[List[str]]) -> List[str]:
        return [board[x][y], board[x + 1][y], board[x + 2][y],
                board[x][y + 1], board[x + 1][y + 1], board[x + 2][y + 1],
                board[x][y + 2], board[x + 1][y + 2], board[x + 2][y + 2]]

    # new system to record the data points. For each digit found, we record three entries (one for each bucket)
    # r1-3 => 3 found at row 1
    # c5-4 => 4 found at column 5
    # b11-9 => 9 found at block 11 (rc)
    def isValidSudokuOptimized(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, r in enumerate(board):
            for j, v in enumerate(r):
                if v != ".":
                    if f"r{i}-{v}" in seen or f"c{j}-{v}" in seen or f"b{i//3}{j//3}-{v}" in seen:
                        return False
                    else:
                        seen.add(f"r{i}-{v}")
                        seen.add(f"c{j}-{v}")
                        seen.add(f"b{i//3}{j//3}-{v}")
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(sol.isValidSudoku(board))
    print(sol.isValidSudokuOptimized(board))
