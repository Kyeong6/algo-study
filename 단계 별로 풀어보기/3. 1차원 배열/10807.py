# 개수 세기

import sys
input = sys.stdin.readline

n = int(input())

# n개만큼의 정수를 공백으로 어떻게 입력받지?
# n개만큼의 조건이 따로 있을 줄 알았는데.. 아니네
# 암기해버리자
n_list = list(map(int, input().split()))

v = int(input())

# count : 리스트 내에 요소 개수 파악 
print(n_list.count(v))