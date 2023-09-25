# 알파벳 찾기

s = list(input())
alp = 'abcdefghijklmnopqrstuvwxyz'

# 이 문제는 기억해두자! 
# 신박한 문제
for i in alp:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')