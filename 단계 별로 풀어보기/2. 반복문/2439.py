# 별 찍기 - 2

import sys
input = sys.stdin.readline

n = int(input())

# 문제 조건에 따른 오른쪽 정렬 필요
# 오른쪽 정렬 : rjust(빈칸개수)
# 주의사항은 rjust(n)을 사용하려면 str()로 묶어준 형태가 필요
for i in range(1, n+1):
    print(str("*"*i).rjust(n), end="\n")
