import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def get_dp_increase(arr):
    dp_increase = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
    return dp_increase

def get_dp_decrease(arr):
    dp_decrease = [1] * n
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[i]:
                dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)
    return dp_decrease

dp_increase = get_dp_increase(arr)
dp_decrease = get_dp_decrease(arr)

max_bitonic_length = 0
for i in range(n):
    max_bitonic_length = max(max_bitonic_length, dp_increase[i] + dp_decrease[i] - 1)

print(max_bitonic_length)