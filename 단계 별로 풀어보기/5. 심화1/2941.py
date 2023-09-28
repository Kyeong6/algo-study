# 크로아티아 알파벳
# 다시 풀기
# 크로아티아 알파벳 리스트에 있는 것처럼 두 개의 글자를 한 글자 취급하는 방법을 모르겠다

# 크로아티아 알파벳 리스트 설정
cr_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 문자 입력
word = input()

# 문자를 변환하는 함수 : replace()
# replace() 함수를 통해 크로아티아 알파벳이 입력값에 있으면 한 글자(*) 취급을 함
for i in cr_alpha:
    word = word.replace(i, '*')
print(len(word))


