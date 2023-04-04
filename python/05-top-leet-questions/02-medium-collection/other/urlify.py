from collections import deque
from typing import List


def urlify(s: List[str]) -> None:
    q = deque()
    for i, c in enumerate(s):
        if c == " ":
            q.append("%")
            q.append("2")
            q.append("0")
        else:
            q.append(c)

        s[i] = q.popleft()


def urlify_alt(s: List[str], true_len: int) -> None:
    index = len(s)-1
    for i in range(true_len-1, -1, -1):
        if s[i] == " ":
            s[index] = "0"
            s[index-1] = "2"
            s[index-2] = "%"
            index -= 3
        else:
            s[index] = s[i]
            index -= 1


if __name__ == "__main__":
    s = [c for c in "Mr John Smith    "]
    print(f"> before: {s=}")
    urlify(s)
    print(f"> after: {s=}")

    s = [c for c in "Mr John Smith    "]
    print(f"> before: {s=}")
    urlify_alt(s, 13)
    print(f"> after: {s=}")
