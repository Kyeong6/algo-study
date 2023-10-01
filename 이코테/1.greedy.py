# 거스름돈

n = 1260 # 원
coin_types = [500, 100, 50, 10]
cnt = 0

# 몫과 나머지로 동전 개수와 잔돈 반환
for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)

# 큰 수의 법칙

n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second 

print(result)
