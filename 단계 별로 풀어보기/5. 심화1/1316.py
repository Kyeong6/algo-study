# 그룹 단어 체커

# 단어의 개수
n = int(input())

# 갯수 파악
group_word = 0

# 문자 입력
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1): # 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]: # 연달은 두 문자가 다른 때,
            new_word = word[index+1:] # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0: # 남은 문자열에서 현재글자가 있었다면
                error += 1 # error 에 1씩 증가
    if error == 0:
        group_word += 1 # error가 0이면 그룹단어
print(group_word)

"""
해결 방법 : 그룹단어를 찾기 위해서 문자열의 알파벳을 하나씩 확인하고 이전 알파벳과
다른 알파벳이 나오는 경우 남아있는 문자열에서 동일한 알파벳이 있는지를 확인해나가는 방식
주요 포인트 : if 조건식에서 연단 두 알파벳을 비교해서 두 알파벳이 다른 경우 남은 문자열을 새로운 단어로
생성하고 count함수로 동일한 알파벳이 있는지를 체크(word -> new_word)

"""
