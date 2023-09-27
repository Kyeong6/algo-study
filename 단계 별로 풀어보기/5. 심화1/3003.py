# 킹,퀸,룩,비숍,나이트,폰

import sys
input = sys.stdin.readline

chess = [1,1,2,2,2,8]

num_list = list(map(int, input().split()))

# 리스트 요소끼리의 사칙연산 하는 방법
res = [chess[i] - num_list[i] for i in range(len(chess))]
print(*res)