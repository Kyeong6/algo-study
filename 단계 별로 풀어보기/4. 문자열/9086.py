# 문자열
# 문자열에서는 import sys는 사용하면 안되는건가?
# 값이 안나온다!
n = int(input())

for i in range(n):
    s = str(input())
    print(s[0]+s[-1])
