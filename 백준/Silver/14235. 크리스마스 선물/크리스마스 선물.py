# https://www.acmicpc.net/problem/14235

import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    num = sys.stdin.readline().strip()
    if num == "0":
        answer = -heapq.heappop(heap) if heap else -1
        print(answer)
    else:
        gifts = list(map(int, num.split()))[1::]
        for gift in gifts:
            heapq.heappush(heap, -gift)
