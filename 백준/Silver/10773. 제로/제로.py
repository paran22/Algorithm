k = int(input())
arr = []
for i in range(k):
    n = int(input())
    if n != 0:
        # 추가
        arr.append(n)
    else:
        # 삭제
        arr.pop()

print(sum(arr))