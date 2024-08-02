import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

days = 0
new_friends_count_list = []
while True:
    answer = 0
    for a in range(1, N + 1):
        answer += len(graph[a])

    if answer == N * (N - 1):
        break

    friend = set()
    for i in range(1, N + 1):
        for j in graph[i]:
            for k in graph[j]:
                if i != k and k not in graph[i]:
                    if i <= k:
                        friend.add((i, k))
                    else:
                        friend.add((k, i))

    for a, b in friend:
        graph[a].append(b)
        graph[b].append(a)

    days += 1
    new_friends_count_list.append(len(friend))

print(days)
for f in new_friends_count_list:
    print(f)
