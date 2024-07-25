# https://www.acmicpc.net/problem/31562


import sys

N, M = map(int, sys.stdin.readline().split())

records = {}


for _ in range(N):
    record = sys.stdin.readline().strip().split()
    records[record[1]] = "".join(record[2:5])

for _ in range(M):
    count = 0
    sound = "".join(sys.stdin.readline().strip().split())
    title = ""
    for name, record in records.items():
        if record == sound:
            count += 1
            title = name

    if count == 0:
        print("!")
    elif count == 1:
        print(title)
    else:
        print("?")
