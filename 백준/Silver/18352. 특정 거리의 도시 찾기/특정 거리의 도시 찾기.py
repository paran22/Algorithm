# https://www.acmicpc.net/problem/18352

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

graph = defaultdict(list)

# 단방향
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

def bfs(start, target_distance):
    visited = [False] * (N + 1)
    distance = [0] * (N + 1)
    answer = []
    queue = deque([start])

    visited[start] = True

    while queue:
        node = queue.popleft()

        for new_node in graph[node]:
            if not visited[new_node]:
                visited[new_node] = True
                queue.append(new_node)
                distance[new_node] = distance[node] + 1
                if distance[new_node] == target_distance:
                    answer.append(new_node)
    return answer

answer = bfs(X, K)

if len(answer) > 0:
    answer.sort()
    for node in answer:
        print(node)
else:
    print(-1)
    

