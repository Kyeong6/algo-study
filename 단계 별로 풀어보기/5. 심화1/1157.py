# 단어 공부
# 다시 풀어봐야 할 문제.. 지금까지 푼 문제 중에 가장 난이도 있음

# 대문자로 변환
word = input().upper()

# 입력받은 문자열에서 중복값 제거
# 입력받은 문자에서 알파벳이 몇 번 사용되는지를 확인하는데 사용
unique_word = list(set(word)) 

# 알파벳이 사용된 횟수를 리스트로 저장
# 인덱스가 몇 개 있는지 파악 : count()
cnt_list = list()
for i in unique_word:
    cnt = word.count(i)
    cnt_list.append(cnt) # count 숫자를 리스트에 append

# print(cnt_list)

"""
숫자 리스트에서 알파벳이 사용된 개수 중 가장 큰 수를 찾고서
해당 숫자가 1보다 크면 물음표 출력.
최대값이 하나라면 숫자 리스트에서 가장 큰 수의 위치를 index함수로 찾고
unique_word 리스트에서 같은 인덱스에 위치한 문자열 출력
unique_word 리스트와 cnt_list의 인덱스는 서로 같다!
"""
if cnt_list.count(max(cnt_list)) > 1: # count 숫자 최대값이 중복되면
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list)) # count 숫자 최대값 인덱스
    # print(max_index)
    print(unique_word[max_index])




