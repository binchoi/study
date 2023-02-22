from typing import List, Set


def solution(numbers: List[int]) -> int:
    square_upper_limit = max(2 * max(numbers), 0)
    full_squares = get_full_squares(min(4 * 10 ** 4, square_upper_limit))
    numbers_set = set(numbers)
    res, singleton_count = 0, 0
    for i in range(len(numbers)):
        for square in full_squares:
            if square - numbers[i] in numbers_set:
                res += 1
                singleton_count += (square - numbers[i] == numbers[i])
    return singleton_count + (res - singleton_count) // 2


def get_full_squares(max_square: int) -> List[int]:
    res = []
    curr, square = 0, 0
    while square <= max_square:
        res.append(square)
        curr += 1
        square = curr ** 2
    return res


