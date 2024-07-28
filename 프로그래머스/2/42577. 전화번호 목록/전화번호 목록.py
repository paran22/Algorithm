def solution(phone_book):
    phone_dict = {}
    for num in phone_book:
        phone_dict[num] = True
        
    for num in phone_book:
        temp = ""
        for digit in num:
            temp += digit
            if temp in phone_dict and temp != num:
                return False
            
    return True