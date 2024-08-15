def solution(keymap, targets):
    answer = []
    for target in targets:
        sum = 0
        for char in target:
            min_count = 0
            hasKey = False
            for key in keymap:
                count = key.find(char)
                if count == -1:
                    continue
                if min_count == 0 or min_count > count:
                    hasKey = True
                    min_count = count + 1
            if not hasKey:
                sum = -1
                break
            sum += min_count
        answer.append(sum)
    return answer