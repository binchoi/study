from typing import List


def solution(arr: List[int]) -> int:
    # transforming arr to diff_arr
    diff_arr = arr_to_diff_arr(arr)
    # print(diff_arr, "diff_arr")
    # iterate through diff_arr and return sawtooth-seq-arr
    sawtooth_seq_len_arr = diff_arr_to_seq_len_arr(diff_arr)
    # print(sawtooth_seq_len_arr)

    res = 0
    for l in sawtooth_seq_len_arr:
        res += (l * (l + 1) / 2)
    return res


def arr_to_diff_arr(arr: List[int]) -> List[int]:
    res = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            res.append("-")
        elif arr[i] > arr[i - 1]:
            res.append("+")
        else:
            res.append(".")
    return res


def diff_arr_to_seq_len_arr(arr: List[int]) -> List[int]:
    res = []
    cnt = 0

    p = 0
    curr = []
    while p < len(arr):
        if arr[p] != "." and (len(curr) == 0 or curr[-1] != arr[p]):
            curr.append(arr[p])
        else:
            if len(curr) > 0:
                res.append(len(curr))
            curr.clear()
            if arr[p] != ".":
                curr.append(arr[p])
        p += 1
    if len(curr) > 0:
        res.append(len(curr))

    return res


