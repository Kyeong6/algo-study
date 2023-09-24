# 바구니 뒤집기

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

num_list = [x for x in range(1,n+1)]

# temp를 사용해야하는 이유는? 
# [::-1] 이렇게 슬라이싱을 이용해서는 못하나?
# 범위가 왜 [i-1:j]인지 알아보기
# Issue에 작성!
for _ in range(m):
    i,j = map(int, input().split())
    temp = num_list[i-1:j]
    temp.reverse()
    num_list[i-1:j] = temp

print(*num_list)

