import sys
 
R, C = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

count = 0
 
def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] > 0:
                stack.append((nx, ny))
                visited[nx][ny] = True
    
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)