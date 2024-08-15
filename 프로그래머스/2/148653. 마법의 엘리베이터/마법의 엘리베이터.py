def solution(storey):
    answer = 0
    while storey != 0:
        count = storey % 10
        if count > 5:
            answer += 10 - count
            storey += 10
        elif count == 5:
            answer += count
            ten = (storey // 10) % 10
            storey += 10 if ten > 4 else 0
        else:
            answer += count
        storey //= 10
    return answer