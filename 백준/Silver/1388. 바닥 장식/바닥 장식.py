# https://www.acmicpc.net/problem/1388

r, c = map(int, input().split())
visits = [[0] * c for _ in range(r)]
array = [list(input()) for _ in range(r)]
d_row = [(0, 1), (0, -1)]
d_column = [(1, 0), (-1, 0)]

count = 0

def dfs(x, y):
    visits[x][y] = 1
    item = array[x][y]
    d = d_row if item == "-" else d_column
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if not visits[nx][ny] and array[nx][ny] == item:
                dfs(nx, ny)
                
for x in range(r):
    for y in range(c):
        if not visits[x][y]:
            dfs(x, y)
            count += 1
            
print(count)