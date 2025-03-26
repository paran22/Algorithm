N = int(input())
words = []

for _ in range(N):
    words.append(input())

words = list(set(words))

# 정렬: 1순위 - 길이, 2순위 - 사전순
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)