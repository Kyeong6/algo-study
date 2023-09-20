# A+B-3

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    c = a + b
    print(c)

# 다른 방식의 출력
# 모든 입력을 다 받은 후 출력을 한 번에 받는 방식 
# How?
import sys
input = sys.stdin.readline

t = int(input())
lst = []

for i in range(t):
    a,b = map(int, input().split())
    c = a + b
    lst.append(c)

print(*lst) # 여기서 세로로 출력을 어떻게 할까?