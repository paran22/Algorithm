import sys
import heapq

N = int(sys.stdin.readline().strip())

dasom = int(sys.stdin.readline().strip())

# 현재 가장 많이 득표한 사람을 찾기 위해 최대힙을 만든다.
heap = [-int(sys.stdin.readline().strip()) for _ in range(N - 1)]
heapq.heapify(heap)

count = 0

while heap and -heap[0] >= dasom:
    # 가장 많은 득표수를 가진 후보의 득표수를 하나 줄이고 다솜이의 득표수를 하나 증가시킨다.
    max_votes = -heapq.heappop(heap)
    dasom += 1
    max_votes -= 1
    heapq.heappush(heap, -max_votes)
    count += 1

print(count)