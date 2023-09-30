# 세로읽기
# 문제 다시 이해하기..

# 먼저 1차원 리스트 설정
words = []
length = []

# 단어와 단어의 길이 입력 받기
for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

rst = ''
# 단어의 길이가 제일 긴 것 기준으로 for문 돌리기
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            rst += words[j][i]

print(rst)
        
