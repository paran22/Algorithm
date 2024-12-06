import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split()) 
M = int(input())

graph = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)

def dfs(node, count):
    if node == B:
        return count
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            result = dfs(next_node, count + 1)
            if result != -1:
                return result
        
    return -1

result = dfs(A, 0)
print(result)