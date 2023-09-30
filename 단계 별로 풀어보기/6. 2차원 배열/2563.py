# 색종이
# 신기한 문제 다시 풀어보자..

# 왜 2차원 리스트를 사용하는 걸까?
# 픽셀 개념!
white_paper = [[0 for j in range(100)] for i in range(100)]

# 색종이 개수
n = int(input())

# 좌표값을 얻기
for i in range(n):
    x, y = list(map(int, input().split()))
    
    # 면적 구하기 : 한 칸당 1씩 출발
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            white_paper[x_idx][y_idx] = 1 # 누적되지 않기 때문에 겹쳐도 1

# 위에서 white_paper[x_idx][y_idx] = 1을 사용해서
# 값이 1인 것들이 존재한다.
# 그래서 아래와 같은 코드를 통해 면적 구하기 가능
counts = 0
for i in white_paper:
    counts = counts + i.count(1)

print(counts)