import sys

N = int(sys.stdin.readline().strip())

stack = []
for i in range(N):
    num = int(sys.stdin.readline().strip())
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)
    
answer = len(stack)
print(answer)