from typing import List

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) excluding output array
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

    def fizzBuzzAlt(self, n: int) -> List[str]:
        return [self.FizzBuzzHelper(i) for i in range(1, n+1)]

    def FizzBuzzHelper(self, i: int) -> str:
        if i % 15 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        return str(i)


if __name__ == "__main__":
    sol = Solution()
    n = 15
    print(sol.fizzBuzz(n))
    print(sol.fizzBuzzAlt(n))
