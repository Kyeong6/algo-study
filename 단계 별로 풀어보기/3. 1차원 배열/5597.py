# 과제 안 내신분..?

import sys
input = sys.stdin.readline

num_list = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    if a in num_list:
        num_list.remove(a)

print(min(num_list))
print(max(num_list))