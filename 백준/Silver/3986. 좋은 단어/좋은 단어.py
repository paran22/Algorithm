import sys
input = sys.stdin.readline

N = int(input())

answer = 0

for _ in range(N):
    words = list(input().strip())
    stack = []
    for word in words:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    answer += 1 if not stack else 0

print(answer)