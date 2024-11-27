T = int(input())

for _ in range(T):
    input()  # 빈 줄 처리
    N, M = map(int, input().split())
    
    # 각 군대의 최강 병사만 찾기
    sj_max = max(map(int, input().split()))
    sb_max = max(map(int, input().split()))
    
    # 최강 병사 비교
    if sj_max >= sb_max:
        print("S")
    else:
        print("B")