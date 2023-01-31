from typing import List, Optional


# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s

class Solution:

    res = []

    # Backtracking (= DFS)
    # Time Complexity: O(n*2^n)
    # Space Complexity: O(n) (if excluding return data)
    def partition(self, s: str) -> List[List[str]]:
        self.res = []  # shared variable across multiple tests should be reset
        self.partition_backtrack(s, 0, [])
        return self.res

    def partition_backtrack(self, s: str, start: int, buf: List[str]):
        if start == len(s):
            self.res.append(buf[:])  # KEY: make slice/copy
            return

        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                buf.append(s[start:end + 1])
                self.partition_backtrack(s, end + 1, buf)
                buf.pop()  # take out the item we previously inserted

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    memo = []

    # Backtracking + Memoization (DP)
    # Time Complexity: O(n*2^n) (but average time complexity is lowered)
    # Space Complexity: O(n*n) (if excluding return data)
    def partitionMemoization(self, s: str) -> List[List[str]]:
        self.res = []
        self.memo: List[List[Optional[bool]]] = [[None] * len(s) for _ in range(len(s))]
        self.partition_backtrack(s, 0, [])
        return self.res

    def partition_backtrack_memoize(self, s: str, start: int, buf: List[str]):
        if start == len(s):
            self.res.append(buf[:])
            return

        for end in range(start, len(s)):
            if self.is_palindrome_memoize(s, start, end):
                buf.append(s[start:end + 1])
                self.partition_backtrack(s, end + 1, buf)
                buf.pop()  # take out the item we previously inserted

    def is_palindrome_memoize(self, s: str, start: int, end: int) -> bool:
        if self.memo[start][end]:
            return self.memo[start][end]
        while start < end:
            if s[start] != s[end]:
                self.memo_palindrome_status(start, end, False)
                return False
            start += 1
            end -= 1
        self.memo_palindrome_status(start, end, True)
        return True

    def memo_palindrome_status(self, start: int, end: int, is_palindrome: bool):
        self.memo[start][end] = is_palindrome
        if is_palindrome:
            while start < end:
                self.memo[start][end] = True
                start += 1
                end -= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
    print(sol.partitionMemoization("aab"))
    print(sol.partition("aaaabcdcbad"))
    print(sol.partitionMemoization("aaaabcdcbad"))

