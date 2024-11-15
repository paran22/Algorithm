import sys

input = sys.stdin.readline

N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

OPPOSITE_INDEX = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

DICE_SIDE_LENGTH = 6

def get_max_side(dice, top_index, bottom_index):
    side_values = [value for i, value in enumerate(dice) if i not in [top_index, bottom_index]]
    return max(side_values)


max_sum = 0
# 첫 번째 주사위의 각 면이 바닥일 때를 모두 시도한다.
for bottom_index in range(DICE_SIDE_LENGTH):
    sum = 0
    
    top_index = OPPOSITE_INDEX[bottom_index]
    bottom = dices[0][bottom_index]
    top = dices[0][top_index]
    
    # 옆 면의 최대값을 구한다.
    sum += get_max_side(dices[0], top_index, bottom_index)
    
    # 그 다음 주사위를 쌓는다.
    for i in range(1, N):
        # 이전 주사위의 윗면 값과 같은 값을 현재 주사위의 아랫면으로 설정한다.
        for j in range(DICE_SIDE_LENGTH):
            if dices[i][j] == top:
                bottom_index = j
                top_index = OPPOSITE_INDEX[bottom_index]
                break
        
        top = dices[i][top_index]

        # 옆 면의 최대값을 구한다.
        sum += get_max_side(dices[i], top_index, bottom_index)
    
    # 저장된 최대값과 비교하여 더 큰 값을 저장한다.
    max_sum = max(max_sum, sum)

print(max_sum)
