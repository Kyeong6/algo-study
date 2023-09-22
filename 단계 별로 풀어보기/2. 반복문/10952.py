# A+B - 5

import sys
input = sys.stdin.readline

lst = []

while True:
    a,b = map(int, input().split())
    if ((a==0) and (b==0)):
        break
    c = a + b
    lst.append(c)
    print(c)
