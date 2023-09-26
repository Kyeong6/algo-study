# 상수

# 수의 크기를 비교하는 문제
# 수를 다른 사람과 다르게 거꾸로 읽음

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

# 입력받은 수를 어떻게 거꾸로 출력할 수 있을까?
# 먼저 문자로 바꿔준 다음에 슬라이싱 후 정수형으로 다시 바꿈
a = int(str(a)[::-1])
b = int(str(b)[::-1])

if (a > b):
    print(a)
else:
    print(b)