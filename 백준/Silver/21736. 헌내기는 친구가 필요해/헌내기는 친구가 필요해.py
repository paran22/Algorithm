# https://www.acmicpc.net/problem/21736

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

# 이동할 수 있는 방향은 상하좌우이다.
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#  O는 빈 공간, X는 벽, I는 도연이(1번만 나온다), P는 사람

graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def dfs(x, y):
    visited[x][y] = True
    count = 0

    if graph[x][y] == "P":
        count += 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] != "X":
            count += dfs(nx, ny)

    return count


def find_start():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "I":
                return i, j
    return None, None


start_x, start_y = find_start()

count = dfs(start_x, start_y)
answer = count if count > 0 else "TT"
print(answer)
