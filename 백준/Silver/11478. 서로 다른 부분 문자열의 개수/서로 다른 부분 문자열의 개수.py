# https://www.acmicpc.net/problem/11478

import sys
sys.setrecursionlimit(10**5)

texts = sys.stdin.readline().strip()

answers = set()

def backTrack(length):
    if length == len(texts) + 1:
        return
    for i in range(len(texts)):
        word = texts[i : i + length]
        answers.add(word)
    backTrack(length + 1)

backTrack(1)

print(len(answers))
