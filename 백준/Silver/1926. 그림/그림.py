# https://www.acmicpc.net/problem/1926

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y):
    visited[x][y] = True
    area = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            area += dfs(nx, ny)

    return area


areas = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            area = dfs(i, j)
            areas.append(area)

print(len(areas))
print(max(areas) if len(areas) > 0 else 0)
