# 문자열 반복

# 횟수 입력
n = int(input())

# 입력할 때 다른 자료형을 어떻게 같이 입력하지?

for _ in range(n):
    r,s = input().split()
    lst = []
    for st in s:
        lst.append(st*int(r))
    print(*lst,sep='')
