import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

extension_dict = defaultdict(int)

for _ in range(N):
    extension = input().rstrip().split('.')[1]
    extension_dict[extension] += 1

for extension, value in sorted(extension_dict.items()):
    print(extension, value)