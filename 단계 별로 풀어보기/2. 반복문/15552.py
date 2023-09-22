# 빠른 A+B

import sys
input = sys.stdin.readline

# 횟수 설정
n = int(input())

lst = []
for i in range(n):
    a,b = map(int, input().split())
    c = a + b
    lst.append(c)

# 출력 요구 사항인 한 줄에 하나씩 출력하기위해 작성
for lsts in lst:
    print(lsts, end="\n") 
