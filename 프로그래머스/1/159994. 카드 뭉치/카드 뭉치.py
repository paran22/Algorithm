from collections import deque

def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    goal_queue = deque(goal)
    while len(goal_queue) > 0:
        word = goal_queue.popleft()
        if queue1 and queue1[0] == word:
            queue1.popleft()
            continue
        if queue2 and queue2[0] == word:
            queue2.popleft()
            continue
        return "No"
    return "Yes"