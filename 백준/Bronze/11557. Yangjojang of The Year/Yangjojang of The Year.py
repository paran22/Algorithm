# https://www.acmicpc.net/problem/11557
import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    N = int(sys.stdin.readline().strip())
    dict = {}
    for i in range(N):
        name, amount = sys.stdin.readline().split()
        dict[name] = int(amount)
    max_key = max(dict, key=dict.get)
    print(max_key)
