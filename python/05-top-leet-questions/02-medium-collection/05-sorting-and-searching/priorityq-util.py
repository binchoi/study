import queue


if __name__ == "__main__":
    q = queue.PriorityQueue()
    q.put(12)
    q.put(1)
    q.put(94)
    q.put(1412)
    q.put(44)
    q.put(-23)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
