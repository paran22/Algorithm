T = int(input())

for _ in range(T):
    expression = input().strip()
    factorial_count = 0
    flag = True
    for word in expression[::-1]:
        if word == '!':
            factorial_count += 1
        else:
            flag = (word == '1')
            break

    for _ in range(factorial_count):
        flag = flag if flag else not flag

    reversed_count = 0
    for word in expression:
        if word == '!':
            reversed_count += 1
        else:
            break

    for _ in range(reversed_count):
        flag = not flag

    answer = int(flag)
    print(answer)