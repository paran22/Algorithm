# 문자열 s를 정수로 변환한다.
def solution(s):
    # 문자열을 정수로 변환하기 위한 dictionary를 생성한다.
    num_dict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    
    # 문자열 s에서 숫자로 변환할 수 있는 문자열을 찾아서 숫자로 변환한다.
    answer = s
    for word, digit in num_dict.items():
        answer = answer.replace(word, digit)
    return int(answer)