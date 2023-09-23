# 공넣기

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# n번까지의 번호가 적힌 박스 설정
box = [0] * n

# m번 실행
# 이중 반복문에서의 범위 주의
# 해당 문제는 바구니에 공이 이미 있는 경우 들어있는 공을 빼고, 새로 공을 넣음
# 횟수 문제가 아니라 최종적으로 박스 내에 있는 값을 출력! (착각했다)
# 문제 제대로 읽기..
for _ in range(m):
    i,j,k = map(int, input().split())
    for p in range(i, j+1):
        # 박스 내에 k를 넣는 방법
        box[p-1] = k

for p in range(n):
    print(box[p], end=" ")

