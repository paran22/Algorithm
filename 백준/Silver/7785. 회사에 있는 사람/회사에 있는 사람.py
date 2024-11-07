import sys
from collections import defaultdict
input = sys.stdin.readline

dictionary = defaultdict(bool)

for _ in range(int(input())):
    name, action = input().split()
    
    if action == 'enter':
        dictionary[name] = True
    else:
        dictionary[name] = False

for name, is_enter in sorted(dictionary.items(), reverse=True):
    if is_enter:
        print(name)