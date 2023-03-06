from typing import List

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a
# different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of
# columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing
# order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        res = [[] for _ in range(r)]

        curr_row = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr_row = self.add_to_matrix(res, curr_row, c, mat[i][j])
        return res

    def add_to_matrix(self, mat: List[List[int]], curr_row: int, c: int, item: int) -> int:
        if len(mat[curr_row]) >= c:
            curr_row += 1
        mat[curr_row].append(item)
        return curr_row

    # using divmod by col simplifies the row-level traversal of matrices
    def matrixReshapeSimplified(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        o_r, o_c = len(mat), len(mat[0])
        if o_r * o_c != r * c:
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r * c):
            r_i, r_j = divmod(i, c)
            o_i, o_j = divmod(i, o_c)
            res[r_i][r_j] = mat[o_i][o_j]
        return res


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4

    print(sol.matrixReshape(mat, r, c))
    print(sol.matrixReshapeSimplified(mat, r, c))

