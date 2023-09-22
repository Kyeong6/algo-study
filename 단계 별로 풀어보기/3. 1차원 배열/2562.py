# 최댓값

import sys
input = sys.stdin.readline

lst = []
for i in range(9):
    a = int(input())
    lst.append(a)

# 최대값의 인덱스 출력 방법 기억하기!
# 리스트명.index(max(리스트명))
print(max(lst))
print(lst.index(max(lst))+1)
