def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        kind = cloth[1]
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 2

    count = 1
    for value in clothes_dict.values():
        count *= value
    return count - 1