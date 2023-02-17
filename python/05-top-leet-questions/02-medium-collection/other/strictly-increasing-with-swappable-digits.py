from typing import List

# You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and
# swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and
# not considered (eg: 010 will be considered just 10).

# Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the
# resulting array are strictly increasing.


def solution(numbers: List[int]) -> bool:
    # make pass and check if strictly greater pattern
    # if pattern is broken (i.e. element is less or eq than previous) -> check flag -> check if can_retain_
    # pattern(numbesr, idx) where idx -1 is greater or eq -> if yes continue(after flagging)
    if len(numbers) < 2:
        return True

    swap_used = False
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            if swap_used:
                return False
            swapped = swap_if_can(numbers, i)
            if not swapped:
                return False
            swap_used = True
    return True


def swap_if_can(numbers: List[int], i: int) -> bool:
    # check i swappable first while comparing to i+1
    if not swap_if_can_helper(numbers, i):
        return swap_if_can_helper(numbers, i - 1)
    return True
    # return swap_if_can_helper(numbers, i) or swap_if_can_helper(numbers, i-1)


def swap_if_can_helper(numbers: List[int], i: int) -> bool:
    lower = numbers[i - 1] if i > 0 else -1
    upper = numbers[i + 1] if i < len(numbers) - 1 else 10 ** 3 + 1
    swapped_val = valid_swap_number(numbers[i], lower, upper)
    if swapped_val != -1:
        numbers[i] = swapped_val
        return True
    return False


def valid_swap_number(num: int, lower: int, upper: int) -> int:
    num_arr = []
    while num > 0:
        div, mod = divmod(num, 10)
        num_arr.append(mod)
        num = div
    num_arr.reverse()
    print(num_arr)
    for i in range(len(num_arr)):
        for j in range(i + 1, len(num_arr)):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
            val = calc_val(num_arr)
            if lower < val < upper:
                return val
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
    return -1

    # can i swap two digits in numbers[i] to make it between this range?
    # 1020 -> 0021
    # 1002 -> 0012


def calc_val(num_arr: List[int]) -> int:
    res = 0
    for i in range(len(num_arr)):
        res = res * 10 + num_arr[i]
    return res


