# A+B - 4

import sys
input = sys.stdin.readline

# 나의 풀이 
# 출력 결과는 맞으나 답이 틀림..
for i in range(5):
    a,b = map(int, input().split())
    c = a + b
    print(c)

# 정답
# 해당 문제는 try, except 구문을 사용해야 함!
# 문제에서 루프의 횟수를 지정 안 해주었기 때문에 except구문 사용 필요

while True:
    try:
        a,b = map(int, input().split())
        c = a + b
    except:
        break
    print(c)