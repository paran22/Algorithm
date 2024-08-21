import sys
N, C = map(int, sys.stdin.readline().split())

array = [0] * (N + 1)
for _ in range(C):
    root, left, right = map(int, sys.stdin.readline().split())
    array[left] = root
    array[right] = root
    
def dfs(p, cnt):
    if p == 1: return cnt
    return dfs(array[p], cnt + 1)

for i in range(1, N + 1):
    print(dfs(i, 1))