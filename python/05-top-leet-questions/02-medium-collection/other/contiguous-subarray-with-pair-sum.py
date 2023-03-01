from typing import List, Tuple


# Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair
# of integers with a sum equal to k.

# More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a
# subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one pair (a[s], a[t]), where:
# s ≠ t
# a[s] + a[t] = k

def solution(a, m, k):
    # find all pairs
    # sort based on fst and filter out ones separated by more than k-1
    # iterate through a until range includes fst and snd of first pair (initialize with snd) just with idx

    # sorted and filtered
    lst_of_pairs = get_pairs(a, k, m)
    # print(lst_of_pairs)
    # e.g. (2,4), (3,5), (5,7) with m=4 -> 14, 25, 36, 47, 58
    # prev = (0,3) 9
    # 2,4 -> (1,4) where fst = snd - (m-1)
    res = 0
    prev_lo, prev_hi = -1, -1
    for p in lst_of_pairs:
        lo = max(prev_lo + 1, p[1] - m + 1)  # so its above lower bound
        hi = lo + m - 1
        if hi >= len(a):
            return res

        shift = min(p[0] - lo + 1, len(a) - hi)
        res += shift  # 2

        prev_lo, prev_hi = lo + shift - 1, hi + shift - 1
    return res


def get_pairs(a: List[int], target: int, m: int) -> List[Tuple[int]]:
    res = []
    memo = {}
    for i in range(len(a)):
        if a[i] in memo:
            for comp_idx in memo[a[i]]:
                # only add valid pairs
                if i - comp_idx < m:
                    res.append((comp_idx, i))

        # update memo hashmap
        if target - a[i] not in memo:
            memo[target - a[i]] = []
        memo[target - a[i]].append(i)

    # sort by fst
    res.sort(key=lambda x: x[0])

    return res


from collections import defaultdict
from typing import List


def solutionCorrect(a, m, k):
    num_subarray_with_sum_k = 0
    cnt_in_subarray = defaultdict(int)
    idx_subarray = defaultdict(int)
    last_index = -1

    for i in range(m):
        if a[i] in idx_subarray:
            num_subarray_with_sum_k = 1
            last_index = idx_subarray[a[i]]
        cnt_in_subarray[a[i]] += 1
        idx_subarray[k - a[i]] = i

    for i in range(m, len(a)):
        cnt_in_subarray[a[i - m]] -= 1
        if cnt_in_subarray[a[i - m]] == 0:
            del idx_subarray[k - a[i - m]]

        if a[i] in idx_subarray:
            num_subarray_with_sum_k += 1
            last_index = max(idx_subarray[a[i]], last_index)
        elif last_index > i - m:
            num_subarray_with_sum_k += 1

        cnt_in_subarray[a[i]] += 1
        idx_subarray[k - a[i]] = i

    return num_subarray_with_sum_k
