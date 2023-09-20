# 주사위 세개

import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

# 조건에 따른 코드 작성 -> 조건에 순서에 따라 결과값이 다를 수 있음을 주의하기 
# a==b==c 조건이 제일 먼저 작성 필요, elif 구문이 먼저 나오면 출력 다름
if (a==b==c): 
    print(10000 + (a*1000))
elif (a==b):
    print(1000 + (a*100))
elif (b==c):
    print(1000 + (b*100))
elif (c==a):
    print(1000 + (a*100))
else:
    print(100*max(a,b,c))
