import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
orders = [[] for _ in range(200_001)]

for i in range(N):
    menus = list(map(int, input().split()))
    for menu in menus[1:]:
        heapq.heappush(orders[menu], i)

menus = list(map(int, input().split()))

eater_counts = [0] * N

for menu in menus:
    if orders[menu]:
        eater = heapq.heappop(orders[menu])
        eater_counts[eater] += 1

print(*eater_counts, sep=' ')