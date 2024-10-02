import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split(' ')))

array.sort()
sum = 0

for i in range(1, n):
    active_questions_count = i if i < k else k
    sum += array[i] * active_questions_count
    
print(sum)