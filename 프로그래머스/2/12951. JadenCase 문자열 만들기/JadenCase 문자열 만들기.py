def solution(s):
    answer = ""
    is_first_word = False
    for word in s:
        if word == " ":
            answer += " "
            is_first_word = False
        elif not is_first_word:
            answer += word.upper()
            is_first_word = True
        else:
            answer += word.lower()
    return answer