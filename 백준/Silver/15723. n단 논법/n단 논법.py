# https://www.acmicpc.net/problem/15723

import sys
from collections import deque

# 전제조건이 들어오는 횟수
N = int(sys.stdin.readline().strip())

prerequisites = {}

# 전제조건을 튜플로 저장한다.
# 전제조건은 a is b와 같은 형태로 입력된다.
for _ in range(N):
    a, b = sys.stdin.readline().strip().split(" is ")
    prerequisites[a] = b

M = int(sys.stdin.readline().strip())

answer = []


def bfs(input, target):
    visited = set()
    queue = deque([input])

    while queue:
        node = queue.popleft()
        # target을 찾으면 True를 리턴한다.
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            # prerequisties에 node가 있으면 queue에 추가한다.
            if node in prerequisites:
                queue.append(prerequisites[node])


for _ in range(M):
    input1, input2 = sys.stdin.readline().strip().split(" is ")
    if bfs(input1, input2):
        print("T")
    else:
        print("F")
