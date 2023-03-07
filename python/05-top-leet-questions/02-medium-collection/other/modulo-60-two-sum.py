from typing import List
from collections import defaultdict


# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally,
# we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = defaultdict(int)
        res = 0
        for t in time:
            res += (m[t % 60] if t % 60 > 0 else m[60])
            m[60 - t % 60] += 1
        return res

    def numPairsDivisibleBy60Array(self, time: List[int]) -> int:
        m = [0] * 60
        res = 0
        for t in time:
            mod = t % 60
            res += m[mod]
            complement = 60 - mod if mod != 0 else 0
            m[complement] += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.numPairsDivisibleBy60([30,20,150,100,40])=}")
    print(f"{sol.numPairsDivisibleBy60([60,60,60])=}")
    print(f"{sol.numPairsDivisibleBy60Array([30,20,150,100,40])=}")
    print(f"{sol.numPairsDivisibleBy60Array([60,60,60])=}")
