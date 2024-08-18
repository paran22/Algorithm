from collections import deque

def solution(priorities, location):
    queue = deque((index, value) for index, value in enumerate(priorities))
    tries = 0
    while queue:
        order, process = queue.popleft()
        if any(process < q[1] for q in queue):
            queue.append((order, process))
            continue
        tries += 1
        if order == location:
            return tries