# X보다 작은 수

import sys
input = sys.stdin.readline

n,x = map(int,input().split())
n_list = list(map(int, input().split()))

lt = []

for lst in n_list:
   if (x > lst):
      lt.append(lst)

print(*lt)
