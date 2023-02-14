from typing import List

# You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1,
# and the second string source contains only lowercase English letters.

# Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:
# * they have equal length,
# * for each 0 in pattern the corresponding letter in the substring is a vowel,
# * for each 1 in pattern the corresponding letter is a consonant.

# Your task is to calculate the number of substrings of source that match pattern.


def solution(pattern, source):
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

