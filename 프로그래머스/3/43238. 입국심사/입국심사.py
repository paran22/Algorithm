def solution(n, times):
    left, right = 1, max(times) * n
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        passed_people = 0
        
        for time in times:
            passed_people += mid // time
            if passed_people >= n:
                break
        
        if passed_people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer