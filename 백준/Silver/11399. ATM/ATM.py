cnt = int(input())
arr = list(map(int, input().split()))

sum = 0
sortedArr = sorted(arr)
for i in range(cnt):
    sum += sortedArr[i] * (cnt - i)

print(sum)