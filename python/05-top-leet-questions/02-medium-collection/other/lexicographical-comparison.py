# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

# Also note that digits are considered lexicographically smaller than letters.


# remove one DIGIT from s or t
# digits < letters.

def solution(s, t):
    res = 0

    for i in range(len(s)):
        if s[i].isdigit():
            prefix = s[:i]
            postfix = s[i + 1:]
            if f"{prefix}{postfix}" < t:
                res += 1

    for i in range(len(t)):
        if t[i].isdigit():
            prefix = t[:i]
            postfix = t[i + 1:]
            if s < f"{prefix}{postfix}":
                res += 1
    return res


