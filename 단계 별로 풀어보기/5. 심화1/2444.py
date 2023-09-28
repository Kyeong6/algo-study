# 별찍기

import sys
input = sys.stdin.readline

n = int(input())

# range()에서 역순으로 출력하는 방법을 아는지가 문제의 핵심
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for k in range(n-1, 0, -1):
    print(" "*(n-k)+"*"*(2*k-1))