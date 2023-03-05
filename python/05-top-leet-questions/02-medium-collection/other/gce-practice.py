from typing import List


def solution1(a):
    res = []
    for i in range(len(a)):
        below = a[i-1] if i > 0 else 0
        upper = a[i+1] if i < len(a)-1 else 0
        res.append(a[i] + below + upper)
    return res


def solution2(pattern, source):
    res = 0
    memo = [None] * len(source)  # vowel->0, consonance->1

    for i in range(len(source) - len(pattern) + 1):
        if is_match(pattern, source, i, memo):
            res += 1
    return res


def is_match(pattern: str, source: str, start_idx: int, memo: List[bool]) -> bool:
    for i in range(len(pattern)):
        if not memo[start_idx + i]:
            memo[start_idx + i] = 0 if source[start_idx + i] in {'a', 'e', 'i', 'o', 'u', 'y'} else 1
        if memo[start_idx + i] != int(pattern[i]):
            return False
    return True


def solution4(numbers: List[int]) -> int:
    res = 0
    memo = [None] * len(source)  # vowel->0, consonance->1

    for i in range(len(source) - len(pattern) + 1):
        if is_match(pattern, source, i, memo):
            res += 1
    return res



if __name__ == "__main__":
    b = solution1([4, 0, 1, -2, 3])
    print(b)






# def solution2(a, m, k):
#     pass
#
#
# def solution3(a, m, k):
#     pass
