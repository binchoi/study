from typing import List

# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of
# flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0] - x[1]))
        res = 0

        override = None
        counter = [0, 0]
        threshold = len(costs) / 2

        for c in costs:
            if override is not None:
                res += c[override]
            else:
                take = 1 if c[0] > c[1] else 0
                res += c[take]

                counter[take] += 1
                if counter[take] >= threshold:
                    override = abs(take - 1)
        return res
