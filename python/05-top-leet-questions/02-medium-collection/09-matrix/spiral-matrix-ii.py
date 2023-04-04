from typing import List

# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num_stack = [i for i in range(n**2, 0, -1)]
        res = [[0 for _ in range(n)] for _ in range(n)]

        row_i, row_j = 0, n
        col_i, col_j = 0, n

        while row_i < row_j and col_i < col_j:
            # traverse l->r top
            for i in range(col_i, col_j):
                res[row_i][i] = num_stack.pop()
            row_i += 1

            if row_i == row_j:
                break

            # traverse down right
            for i in range(row_i, row_j):
                res[i][col_j-1] = num_stack.pop()
            col_j -= 1

            # traverse r->l bottom
            for i in range(col_j-1, col_i-1, -1):
                res[row_j-1][i] = num_stack.pop()
            row_j -= 1

            # traverse up left
            for i in range(row_j-1, row_i-1, -1):
                res[i][col_i] = num_stack.pop()
            col_i += 1

        return res

    def generateMatrixGeneral(self, n: int) -> List[List[int]]:
        num_stack = [i for i in range(n**2, 0, -1)]
        res = [[0 for _ in range(n)] for _ in range(n)]

        row_i, row_j = 0, n
        col_i, col_j = 0, n

        while row_i < row_j and col_i < col_j:
            # traverse l->r top
            for i in range(col_i, col_j):
                res[row_i][i] = num_stack.pop()
            row_i += 1

            # traverse down right
            for i in range(row_i, row_j):
                res[i][col_j-1] = num_stack.pop()
            col_j -= 1

            # traverse r->l bottom
            if row_i < row_j:
                for i in range(col_j-1, col_i-1, -1):
                    res[row_j-1][i] = num_stack.pop()
            row_j -= 1

            # traverse up left
            if col_i < col_j:
                for i in range(row_j-1, row_i-1, -1):
                    res[i][col_i] = num_stack.pop()
            col_i += 1

        return res


if __name__ == "__main__":
    sol = Solution()

    print("\n".join(str(a) for a in sol.generateMatrix(5)))
    print("\n".join(str(a) for a in sol.generateMatrix(8)))
