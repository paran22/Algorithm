while (1):

    vps = input()
    if vps == '.':
        break

    stack_check_list = []
    check = True
    for i in vps:
        if i == '(':
            stack_check_list.append(0)
        elif i == '[':
            stack_check_list.append(1)
        elif i == ')':

            if not stack_check_list:
                check = False
                break
            if stack_check_list.pop() != 0:  # 엇갈렸을때
                check = False
                break
        elif i == ']':
            if not stack_check_list:
                check = False
                break
            if stack_check_list.pop() != 1:  # 엇갈렸을때
                check = False
                break
    if not stack_check_list and check:
        print("yes")
    else:
        print("no")