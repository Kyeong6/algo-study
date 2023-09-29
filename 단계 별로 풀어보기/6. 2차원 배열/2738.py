# 행렬 덧셈
# 문제 유형 다시 파악

import sys
input = sys.stdin.readline

# 먼저 리스트를 하나 만들기
a, b =[], []

n,m = map(int, input().split())

# 미리 설정한 리스트에 반복문을 이용해서 얻은 리스트 넣기
for row in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    b.append(row)

# 출력하는 방법
for row in range(n):
    for col in range(m):
        print(a[row][col] + b[row][col], end=' ')
    print()



