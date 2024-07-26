# https://www.acmicpc.net/problem/11478

import sys

texts = sys.stdin.readline().strip()

answers = set()

for i in range(len(texts)):
    for j in range(i, len(texts)):
        answers.add(texts[i:j+1])

print(len(answers))
