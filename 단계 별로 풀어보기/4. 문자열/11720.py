# 숫자의 합

n = input()
nums = input()
sum = 0

# 문자로 입력받았기 때문에 정수형으로 변환 후 계산
for i in nums:
    sum = sum + int(i)
print(sum)

