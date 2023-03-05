# You are given an array of integers a, where each element a[i] represents the length of a ribbon.
#
# Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.
#
# Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.

# def solution(a, k):
#     size, count = 0, 10**9
#     while count >= k:
#         size += 1
#         count = total_ribbons_of_fixed_size(a, size)
#     return size - 1

def solution(a, k):
    # size of ribbon
    lo, hi = 0, max(a)
    while lo < hi:
        mid = (lo + hi) // 2 + 1
        ribbon_count = total_ribbons_of_fixed_size(a, mid)
        if ribbon_count >= k:
            lo = mid
        else:
            hi = mid - 1
    return lo


# 1 4 2 3 5 929 234  2193 249 4949 494 49 39 393 391
# k = 10

# 1 2 3 4 10
# k = 3 -> start at third from largest as size => 3
# 1 1 1 1 1000000 k = 2 -> 500000
# 1 1 1 4 1000000 k = 3 -> 333333

def total_ribbons_of_fixed_size(a, size):
    return sum(l // size for l in a) if size > 0 else 10 ** 9


def solution_two(a, k):
    a.sort(reverse=True)
    max_len = a[0]
    min_len = a[k - 1] if k - 1 < len(a) else 1

    while min_len < max_len:
        mid_len = (max_len + min_len) // 2 + 1  # right bias
        max_count = get_max_count(a, mid_len)
        print(max_count)
        if max_count >= k:
            min_len = mid_len
        else:
            max_len = mid_len - 1
    return min_len


def get_max_count(a, l):
    count = 0
    for a_i in a:
        count += a_i // l
    return count
