import heapq


if __name__ == "__main__":
    arr = [5, 2, 1, 4, 3]
    heapq.heapify(arr)  # O(n)

    print("heap:", arr)

    print("pop:", heapq.heappop(arr))
    print("pop:", heapq.heappop(arr))

    print(arr)
    print(heapq.heappush(arr, -10))
    print(arr)

    print("pop:", heapq.heappop(arr))

