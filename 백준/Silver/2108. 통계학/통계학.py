# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

input = sys.stdin.readline

def get_average(arr):
    return round(sum(arr) / len(arr))

def get_medium(arr):
    return sorted(arr)[len(arr)//2]

def get_most_frequent(arr):
    count = Counter(arr)
    
    most_common_arr = count.most_common()
    max_frequency = most_common_arr[0][1]
    most_frequent_values = sorted(num for num, freq in most_common_arr if freq == max_frequency)

    has_multiple_frequency = len(most_frequent_values) > 1

    return most_frequent_values[1] if has_multiple_frequency else most_frequent_values[0]

def get_range(arr):
    sortedArr = sorted(arr)
    return sortedArr[-1] - sortedArr[0]

N = int(input())
arr = [int(input()) for _ in range(N)]

print(get_average(arr))
print(get_medium(arr))
print(get_most_frequent(arr))
print(get_range(arr))