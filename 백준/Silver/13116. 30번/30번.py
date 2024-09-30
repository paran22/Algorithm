import sys, math
input = sys.stdin.readline

N = int(input())

def getLevel(value):
    return math.floor(math.log2(value))

for _ in range(N):
    a, b = map(int, input().split())
    
    while True:
        levelA, levelB = getLevel(a), getLevel(b)
        if levelA == levelB:
            break
        if levelA > levelB:
            a //= 2
        elif levelA < levelB:
            b //= 2
    
    while a != b:
        a //= 2
        b //= 2
    
    print(a * 10)
        