from collections import Counter

# You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two
# different indices i < j, such that a[i] + a[j] is divisible by k.


# Optimal - TODO: investigate further
def solution(a, k):
    count = 0
    freq = {}
    for num in a:
        rem = num % k
        count += freq.get((k - rem) % k, 0)
        freq[rem] = freq[rem] + 1 if rem in freq else 1
    return count


def solution_initial(a, k):
    if k == 1:
        return combination_choose_two(len(a))

    modulo_dict = Counter(item % k for item in a)
    res = 0

    # 0 - nC2
    if 0 in modulo_dict:
        res += combination_choose_two(modulo_dict[0])

    for i in range(1, k // 2 + 1):
        if k - i == i and i in modulo_dict:
            res += combination_choose_two(modulo_dict[i])
        else:
            res += (modulo_dict.get(i, 0) * modulo_dict.get(k - i, 0))

    return res


def combination_choose_two(n: int) -> int:
    return n * (n - 1) / 2 if n > 1 else 0  # O(1)


