# 알림 시계

import sys
input = sys.stdin.readline

# 시간, 분 입력받기
h, m = map(int, input().split())

# 시간의 순환주기에 따라 수가 다시 돌아가는 것 이해하기
# m의 45분 기준으로인해 h가 바뀜
# m이 45보다 작을때 h가 0이라면 23시로 바뀌는 것 주의 
if (m < 45):
    if (h == 0):
        print(23, 60-(45-m), sep=" ")
    else:
        print(h-1, 60-(45-m), sep=" ")
else:
    print(h, m-45, sep=" ")