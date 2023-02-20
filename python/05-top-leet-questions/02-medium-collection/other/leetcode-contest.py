class Solution:

    def minHelper(self, s: str) -> int:
        to_replace = '-'
        s_arr = [*s]
        for i in range(len(s_arr)):
            if s_arr[i] == '0':
                continue
            if to_replace == '-':
                to_replace = s_arr[i]

            if s_arr[i] == to_replace:
                s_arr[i] = '0'
        return int("".join(s_arr))

    def maxHelper(self, s: str) -> int:
        to_replace = '-'
        s_arr = [*s]
        for i in range(len(s_arr)):
            if s_arr[i] == '9':
                continue
            if to_replace == '-':
                to_replace = s_arr[i]
            if s_arr[i] == to_replace:
                s_arr[i] = '9'
        return int("".join(s_arr))

    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        return self.maxHelper(s) - self.minHelper(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMaxDifference(11891))
    print(sol.minMaxDifference(90))
