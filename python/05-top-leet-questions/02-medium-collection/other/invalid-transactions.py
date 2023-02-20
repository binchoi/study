from typing import List, Dict, Tuple

# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing
# the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.



class Solution:
    # name, time, amount, and city
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res_idx = set()
        t_map: Dict[str, List[Tuple[List[str], int]]] = {}
        for i, t in enumerate(transactions):
            t_arr = self.transaction_to_array(t)
            if int(t_arr[2]) > 1000:
                res_idx.add(i)

            if t_arr[0] not in t_map:
                t_map[t_arr[0]] = [(t_arr, i)]
            else:
                for t_existing in t_map[t_arr[0]]:
                    if -60 <= int(t_existing[0][1]) - int(t_arr[1]) <= 60 and t_existing[0][3] != t_arr[3]:
                        res_idx.add(t_existing[1])
                        res_idx.add(i)

                t_map[t_arr[0]].append((t_arr, i))

        return [t for i, t in enumerate(transactions) if i in res_idx]

    def transaction_to_array(self, transaction: str) -> List[str]:
        return transaction.split(",")

    def array_to_transaction(self, arr: List[str]) -> str:
        return ",".join(arr)


