# 파일을 읽고 단어를 카운팅해 가장 많이 나온 단어 찾기
'''
구현순서
1. 파일을 읽어들임
2. 단어들과 카운팅을 담을 딕셔너리 생성
3. 파일의 한줄씩 읽어 (2)의 딕셔너리 채우기
4. 가장 많이 나온 단어 찾는 함수
5. 가장 많이 나온 단어와 수를 출력
'''

fhand = open('crown.txt')
strings = fhand.readline().split()

def find_max(line):
    fdic = {}
    count = 0
    word = ''
    for i in line:  #해당 for문대신 딕셔너리명.get()을 사용할 수 있음.
        if i in fdic:
            fdic[i] = fdic[i]+1
        else:
            fdic[i] = 0
    for i in fdic:
        if fdic[i] > count:
            count = fdic[i]
            word = i
    return word, count

word1, count1 = find_max(strings)
print(word1, count1)