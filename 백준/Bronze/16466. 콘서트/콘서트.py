# https://www.acmicpc.net/problem/16466

import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
array_set = set(array)

for i in range(1, N + 1):
    if i not in array_set:
        print(i)
        sys.exit()

print(N + 1)
