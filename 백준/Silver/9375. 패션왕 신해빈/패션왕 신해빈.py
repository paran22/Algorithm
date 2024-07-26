# https://www.acmicpc.net/problem/9375

import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    cloths = {}
    n = int(sys.stdin.readline().strip())
    for j in range(n):
        input = sys.stdin.readline().rstrip().split()
        name = input[0]
        kind = input[1]
        if kind in cloths:
            cloths[kind].append(name)
        else:
            cloths[kind] = [name]

    count = 1
    for _, items in cloths.items():
        count *= len(items) + 1
    print(count - 1)
