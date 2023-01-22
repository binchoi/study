view = None


class Solution:

    def __init__(self, field):
        self.field = field
        self.view = [[-1] * len(field[0]) for i in range(len(field))]

    def solve(self, x, y):
        self.update_view(x, y)
        return self.view

    def update_view(self, x: int, y: int):
        if self.view[x][y] != -1:
            return

        cnt = self.count_surrounding_mines(x, y)
        self.view[x][y] = cnt

        if cnt != 0:
            return

        if y > 0:
            # l
            self.update_view(x, y - 1)
            # lu
            if x > 0:
                self.update_view(x - 1, y - 1)
            # ld
            if x < len(self.field) - 1:
                self.update_view(x + 1, y - 1)
        if y < len(self.field[0]) - 1:
            # r
            self.update_view(x, y + 1)
            # ru
            if x > 0:
                self.update_view(x - 1, y + 1)
            # rd
            if x < len(self.field) - 1:
                self.update_view(x + 1, y + 1)
        # up
        if x > 0:
            self.update_view(x - 1, y)
        # down
        if x < len(self.field) - 1:
            self.update_view(x + 1, y)

    def count_surrounding_mines(self, x: int, y: int):
        return self.is_mine(x - 1, y - 1) + self.is_mine(x - 1, y) + self.is_mine(x - 1, y + 1) + \
               self.is_mine(x, y - 1) + self.is_mine(x, y + 1) + \
               self.is_mine(x + 1, y - 1) + self.is_mine(x + 1, y) + self.is_mine(x + 1, y + 1)

    def is_mine(self, x: int, y: int):
        if x < 0 or x > len(self.field) - 1 or y < 0 or y > len(self.field[0]) - 1:
            return 0
        return int(self.field[x][y])


def solution(field, x, y):
    sol = Solution(field)
    return sol.solve(x, y)


if __name__ == '__main__':
    field = [[True, True, True],
             [True, True, True],
             [True, True, True]]

    print(solution(field, 1, 1))

    field = [[True, True, True],
             [True, False, False],
             [True, False, False]]

    view = solution(field, 2, 2)
    for v in view:
        print(v)

