# 최댓값

# 2차원 리스트 형성을 위한 리스트 형성
a = list() 

# 2차원 리스트 형성
for row in range(9):
    num = list(map(int, input().split()))
    a.append(num)

# 최대값 (암기 필요) -> map()을 왜 사용하나?
# map() : iterable을 받아서, 각 요소에 함수를 적용해주는 함수
# map(적용시킬함수, (적용할 요소들))
max_value = max(map(max, a))
print(max_value)

# 최대값 인덱스(여기서 막혔다..)

# 정답
field = list()

for _ in range(9):
    field.append(list(map(int, input().split())))

max_value = 0
row = 0
col = 0

# 계속 갱신되어서 값을 찾음 -> 탐색
for i in range(9):
    for j in range(9):
        if field[i][j] >= max_value:
            max_value = field[i][j]
            row = i+1
            col = j+1

print(max_value)
print(row, col)