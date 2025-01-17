import sys

input = sys.stdin.readline

LINE_LEN = 5
MAX_LETTER_LEN = 15

lines = [input().rstrip() for _ in range(LINE_LEN)]

max_len = max(len(line) for line in lines)

lines = [line.ljust(max_len, ' ') for line in lines]

answer = ''

for i in range(max_len):
    for line in lines:
        answer += line[i]

print(answer.replace(' ', ''))