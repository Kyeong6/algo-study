# 오븐 시계

import sys
input = sys.stdin.readline

# 시, 분, 시간 입력
h, m = map(int, input().split())
t = int(input())

if (m+t > 60):
    if (h != 23):
        print(h+1, (m+t)-60, sep=" ")
    else:
        print(0, (m+t)-60, sep=" ")

elif (m+t % 60 == 0):
    circle = h+(m+t//60)
    if (circle > 24):
        print((m+t//60), 0, sep=" ") 
    elif (circle == 24):
        print(0, 0, sep=" ")

else:
    print(h, (m+t), sep=" ")

# 정답
'''
추가적인 입력 값:
23 59 \n 1 => output : 0 0
25 0 \n 60 => output : 2 0
22 59 \n 1000 => output : 15 39
23 59 \n 120 => output : 1 59

1. 필요한 시간인 c와 기존 분 b를 더했을 때 60이 넘는다면 60분으로 나눈 몫만큼 시간 더해주기
2. 시계 특성상 23시 59분에서 1분이 지나면 0시 0분이 되기 때문에 a값이 24를 넘어가면 0으로 초기화되면서 시간 더해주기 
'''

import sys
input = sys.stdin.readline

# 시, 분, 시간 입력
a, b = map(int, input().split())
c = int(input())

hour = (b+c)//60
min = (b+c)%60

if (b+c >= 60):
    if(a+hour >= 24):
        a = a - 24 
    a = a + hour # 굳이 else문 사용 안 해도 됨
    print(a, min)

else:
    if (a >= 24):
        a = a - 24
    print(a, b+c)

