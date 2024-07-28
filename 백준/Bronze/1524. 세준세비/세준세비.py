# https://www.acmicpc.net/problem/1524

import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    sys.stdin.readline()
    S, B = map(int, sys.stdin.readline().split())
    S_soldiers = sorted(list(map(int, sys.stdin.readline().split())))
    B_soldiers = sorted(list(map(int, sys.stdin.readline().split())))
    
    s_index, b_index = 0, 0  # 인덱스를 사용하여 리스트 순회
    while s_index < len(S_soldiers) and b_index < len(B_soldiers):
        if S_soldiers[s_index] < B_soldiers[b_index]:
            s_index += 1
        else:
            b_index += 1
    
    if s_index < len(S_soldiers):
        print("S")
    elif b_index < len(B_soldiers):
        print("B")
    else:
        print("C")