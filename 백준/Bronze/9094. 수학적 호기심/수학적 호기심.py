import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())
dict = defaultdict(dict)

for b in range(2, 101):
    for a in range(1, b):
        dict[b][a] = a**2 + b**2

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    count = 0
    for b in range(2, n):
        for a in range(1, b):
            if (dict[b][a] + m) % (a * b) == 0:
                count += 1
    print(count)