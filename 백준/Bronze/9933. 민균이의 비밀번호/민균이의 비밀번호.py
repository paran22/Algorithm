# https://www.acmicpc.net/problem/9933

import sys

N = int(sys.stdin.readline().strip())

array = [sys.stdin.readline().strip() for _ in range(N)]

reversed_array = map(lambda s: s[::-1], array)

for word in array:
    if word[::-1] in array:
        print(f"{len(word)} {word[len(word) // 2]}")
        sys.exit()
