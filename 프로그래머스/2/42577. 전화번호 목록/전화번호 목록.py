def solution(phone_book):
#     sorted_phone_book = sorted(phone_book, key=len)
#     length = len(phone_book)
    
#     for i in range(0, length):
#         for j in range(i + 1, length):
#             prefix, number = sorted_phone_book[i], sorted_phone_book[j]
#             if len(prefix) > len(number):
#                 break
#             if number.startswith(prefix):
#                 return False
#     return True
    phone_book_dict = {value: True for value in phone_book}

    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[0:i]
            if prefix in phone_book_dict:
                return False
            
    return True