import sys

input = sys.stdin.readline

N = int(input())
skills = list(input().strip())

stackL = []
stackS = []
count = 0

for skill in skills:
    if skill == 'L':
        stackL.append(skill)
    elif skill == 'S':
        stackS.append(skill)
    elif skill == 'R':
        if stackL:
            stackL.pop()
            count += 1
        else:
            break
    elif skill == 'K':
        if stackS:
            stackS.pop()
            count += 1
        else:
            break
    else:
        count += 1

print(count)