# https://www.acmicpc.net/problem/1524

import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    sys.stdin.readline()
    S, B = map(int, sys.stdin.readline().split())
    S_soldiers = sorted(list(map(int, sys.stdin.readline().split())))
    B_soldiers = sorted(list(map(int, sys.stdin.readline().split())))
    while len(S_soldiers) != 0 and len(B_soldiers) != 0:
        if S_soldiers[0] < B_soldiers[0]:
            del S_soldiers[0]
        else:
            del B_soldiers[0]
    if len(S_soldiers) > len(B_soldiers):
        print("S")
    elif len(S_soldiers) < len(B_soldiers):
        print("B")
    else:
        print("C")
