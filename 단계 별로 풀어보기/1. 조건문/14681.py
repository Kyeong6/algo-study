# 사분면 고르기

import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

# elif를 사용해서 조건에 따른 문장 하나씩 작성하는 것보다 중첩조건문 사용해서 해결
if (x > 0):
    if (y > 0):
        print('1')
    else:
        print('4')
elif (x < 0):
    if (y > 0):
        print('2')
    else:
        print('3')