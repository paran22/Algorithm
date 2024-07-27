import sys
import itertools

array = [int(sys.stdin.readline().strip()) for _ in range(9)]

for i in itertools.combinations(array, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        sys.exit()