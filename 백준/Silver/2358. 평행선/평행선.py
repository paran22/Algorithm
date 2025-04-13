import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

x_coords = defaultdict(int)
y_coords = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    x_coords[x] += 1
    y_coords[y] += 1

answer = 0
for count in x_coords.values():
    if count >= 2:
        answer += 1
for count in y_coords.values():
    if count >= 2:
        answer += 1

print(answer)
    