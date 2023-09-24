# 평균

import sys
input = sys.stdin.readline

# 과목 갯수
n = int(input())

# 과목에 따른 시험 성적
n_list = list(map(int, input().split()))

# 새로운 값을 담을 자료구조
li = list()

# 새로운 평균 수식
mx = max(n_list)
for lst in n_list:
    avg = lst/mx*100
    li.append(avg)

print(sum(li)/len(li))