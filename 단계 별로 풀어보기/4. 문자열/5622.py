# 다이얼

# 1이 제일 가까운데 2초가 걸림
# 다이얼 수가 옆으로 넘어갈수록 +1 추가

# 이 문제는 다시 풀어보기!!
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()
ret = 0
# 입력받은 문자 개수 파악
for j in range(len(s)):
    # 다이얼 내부에 있는 문자 파악
    for i in dial:
        if s[j] in i:
            ret += dial.index(i)+3
print(ret)


