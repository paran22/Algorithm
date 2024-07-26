# https://www.acmicpc.net/problem/31562


import sys

N, M = map(int, sys.stdin.readline().split())

records = {}


for _ in range(N):
    record = sys.stdin.readline().strip().split()
    record_sound = "".join(record[2:5])
    record_title = record[1]
    if record_sound in records:
        records[record_sound].append(record_title)
    else:
        records[record_sound] = [record_title]

for _ in range(M):
    sound = "".join(sys.stdin.readline().strip().split())
    titles = records.get(sound, [])
    if len(titles) == 0:
        print("!")
    elif len(titles) == 1:
        print(titles[0])
    else:
        print("?")
