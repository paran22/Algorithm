def solution(s):
    # ")"로 시작하면 올바른 괄호가 아니다.
    if s[0] == ")":
        return False

    pare = 0
    for char in s:
        if char == "(":
            pare += 1
        else:
            if pare == 0:
                return False
            pare -= 1
            
    return pare == 0