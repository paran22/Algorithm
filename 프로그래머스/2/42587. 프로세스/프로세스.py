from collections import deque

def solution(priorities, location):
    queue = deque((index, value) for index, value in enumerate(priorities))
    tries = 0
    while queue:
        max_priority = max(queue, key=lambda x: x[1])[1]
        order, process = queue.popleft()
        if max_priority > process:
            queue.append((order, process))
            continue
        tries += 1
        if order == location:
            return tries