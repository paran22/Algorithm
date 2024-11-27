def solution(citations):
    # 각 횟수에 대해 인용된 횟수를 화인하기 위해 내림차순으로 정렬한다.
    # 예를 들어 [6, 5, 3, 1, 0]이라면 
    # 6회 이상 인용된 논문은 1(index + 1)개, 5회 이상 인용된 논문은 2(index + 1)개이다.
    citations.sort(reverse=True)
    h_index = 0

    for i, citation_count in enumerate(citations):
        cited_article_count = i + 1
        # 인용된 횟수가 논문 수보다 많거나 같으면 h_index를 갱신한다.
        if citation_count >= cited_article_count:
            h_index = cited_article_count
    return h_index