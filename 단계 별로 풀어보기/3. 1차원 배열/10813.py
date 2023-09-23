# 공 바꾸기

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 각각의 박스는 1번부터 n번까지 번호 매겨짐
# 처음에는 박스에 적혀있는 번호와 같은 번호 적힌 공 들어있음

# 리스트 함축으로 간결하게 작성 가능
box = [i for i in range(1, n+1)]

# box = []
# for i in range(1, n+1):
#     box.append(i

# 어떻게 바꿀 것인가?에 대한 코드 작성
# temp라 변수에 담을 수 있지만 파이썬에서는 다르게 표현 가능

for _ in range(m):
    i,j = map(int, input().split())
    # 인덱스는 0부터 시작하므로 -1을 해줘야지 접근 가능
    box[i-1], box[j-1] = box[j-1], box[i-1]

print(*box, end=" ")