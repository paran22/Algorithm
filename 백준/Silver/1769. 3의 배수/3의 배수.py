# https://www.acmicpc.net/problem/1769

import sys

num_str = sys.stdin.readline().strip()

count = 0

while len(num_str) > 1:
    sum = 0
    count += 1
    for num in num_str:
        sum += int(num)
    num_str = str(sum)
    
if int(num_str) % 3 == 0:
    is_3_multiple = 'YES'
else:
    is_3_multiple = 'NO'
    
print(count)
print(is_3_multiple)
