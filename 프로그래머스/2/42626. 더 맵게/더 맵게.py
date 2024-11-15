import heapq

def solution(scoville, K):
    # 최소 값을 확인하기 위해 최소힙을 만든다.
    heapq.heapify(scoville)
    count = 0
    
    # 음식이 2개 이상이고 가장 맵지 않은 음식이 K보다 작으면 새로운 음식을 만든다.
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1
        
    # 가장 스코빌이 작은 음식이 K보다 크거나 같은지 확인한다.
    min_scoville = scoville[0]
    reached_target_scoville = min_scoville >= K

    # reached_target_scoville가 true이면 count를, false이면 -1을 반환한다.
    return count if reached_target_scoville else -1