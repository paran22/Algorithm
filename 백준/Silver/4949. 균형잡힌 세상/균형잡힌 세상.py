while (1):

    vps = input()
    if vps == '.':
        break

    stack_check_list = []
    check = 1
    for i in vps:
        if i == '(':
            stack_check_list.append(0)
        elif i == '[':
            stack_check_list.append(1)
        elif i == ')':

            if len(stack_check_list) == 0:
                check = 0
                break
            if stack_check_list.pop() != 0:  # 엇갈렸을때
                check = 0
                break
        elif i == ']':
            if len(stack_check_list) == 0:
                check = 0
                break
            if stack_check_list.pop() != 1:  # 엇갈렸을때
                check = 0
                break
    if len(stack_check_list) == 0 and check:
        print("yes")
    else:
        print("no")