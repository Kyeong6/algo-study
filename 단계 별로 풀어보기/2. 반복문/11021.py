# A+B - 7

import sys
input = sys.stdin.readline

t = int(input())

# 문제에서 주어진 출력을 보면 한 번에 출력처럼 보이지만
# 입력 후 바로 출력이여서 다음과 같이 코드 작성 가능
for i in range(1, t+1):
    a,b = map(int, input().split())
    c = a + b
    print("Case #{}: {}".format(i, c))