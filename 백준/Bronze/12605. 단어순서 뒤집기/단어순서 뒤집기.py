# https://www.acmicpc.net/problem/12605

import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    origin = sys.stdin.readline().split()
    origin.reverse()
    print(f'Case #{i + 1}: {" ".join(origin)}')