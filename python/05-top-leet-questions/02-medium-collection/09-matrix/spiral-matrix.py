from typing import List

# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_i, row_j = 0, len(matrix)  # exclusive upper bound
        col_i, col_j = 0, len(matrix[0])  # exclusive

        while row_i < row_j and col_i < col_j:
            # across the top
            for i in range(col_i, col_j):
                res.append(matrix[row_i][i])
            row_i += 1

            # down the right
            for i in range(row_i, row_j):
                res.append(matrix[i][col_j - 1])
            col_j -= 1

            # across the bottom (right->left)
            if row_i < row_j:
                for i in range(col_j - 1, col_i - 1, -1):
                    res.append(matrix[row_j - 1][i])
            row_j -= 1

            # up the left
            if col_i < col_j:
                for i in range(row_j - 1, row_i - 1, -1):
                    res.append(matrix[i][col_i])
            col_i += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    print(sol.spiralOrder(matrix))
    print(sol.spiralOrder(matrix_2))
