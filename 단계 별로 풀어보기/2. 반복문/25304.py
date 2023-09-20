# 영수증

import sys
input = sys.stdin.readline

x = int(input())
n = int(input())

lst = []

for i in range(n):
    a,b = map(int, input().split())
    hap = a * b
    lst.append(hap)

if (sum(lst) == x):
    print("Yes")
else:
    print("No")