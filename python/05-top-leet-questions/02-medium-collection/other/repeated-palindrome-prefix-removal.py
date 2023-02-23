from typing import List

# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step
# with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not
# familiar with them.


def solution(s: str) -> str:
    s_arr = [c for c in s]
    start, end = helper(s_arr, 0)
    return s[start:end]


# returns start, end (exclusive)
def helper(s_arr: List[str], start: int) -> (int, int):
    end = get_longest_palindrome(s_arr, start)  # end idx (exclusive)
    if end - start <= 1:
        return start, len(s_arr)
    return helper(s_arr, end)


def get_longest_palindrome(s_arr: List[str], start: int) -> int:
    res = start
    for i in range(start, len(s_arr)):
        lo, hi = start, i
        while lo < hi:
            if s_arr[lo] != s_arr[hi]:
                break
            lo += 1
            hi -= 1
        if lo >= hi:
            res = i + 1
    return res
