# https://www.acmicpc.net/problem/16173

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visits = [[0] * n for _ in range(n)]
d_x = [1, 0]
d_y = [0, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visits[x][y] = 1

    while q:
        x, y = q.popleft()
        step = graph[x][y]

        if graph[x][y] == -1:
            return True
        for move in range(2):
            nx = x + d_x[move] * step
            ny = y + d_y[move] * step

            if 0 <= nx < n and 0 <= ny < n and not visits[nx][ny]:
                visits[nx][ny] = 1
                q.append([nx, ny])


if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
