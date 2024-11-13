from collections import deque

N = int(input())
cards = deque(range(1, N+1))  # 1부터 N까지의 카드
discardedCards = []  # 버린 카드들을 저장할 리스트

while len(cards) > 1:
    # 제일 위의 카드를 버린다.
    topCard = cards.popleft()
    discardedCards.append(topCard)
    
    # 그 다음 제일 위의 카드를 제일 아래로 옮긴다.
    if cards:
        topCard = cards.popleft()
        cards.append(topCard)

# 마지막 남은 카드를 discardedCards에 추가한다.
lastCard = cards.popleft()
discardedCards.append(lastCard)

print(*discardedCards)