# 너의 평점은

# 과목명, 학점, 등급
# 전공평점 : (학점 x 과목평점)의 합 / 학점의 총합

rating = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]

total = 0 # 학점 총합을 담을 변수
res = 0 # (학점 x 과목평점) 총합을 담을 변수

for _ in range(20):
    s,p,g = input().split()
    p = float(p)
    if g != 'P':
        total += p
        res += p*grade[rating.index(g)] # rating과 grade는 인덱스에 맞게 구성되어있음

print('%.6f' % (res / total))

# 해당 문제를 리스트가 아닌 딕셔너리로 푼다면? -> 시간이 좀 덜 걸리고 코드가 깔끔하다.
total = 0
res = 0

rating = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

for _ in range(20):
    subject,score,grade = input().split()
    if grade == 'P':
        continue
    total += float(score)
    res += float(score) * rating[grade] # value값이 나옴

print('%.6f' % (res / total))