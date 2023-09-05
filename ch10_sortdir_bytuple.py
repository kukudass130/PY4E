#(정렬_ 모든 단어와 언급된 수)구현 순서
#조건: .items() / .get() 함수 사용하기
'''
1. 파일명 입력받고 파일 열기
2. 파일 한줄씩 받아 읽고 단어 쪼개기
3. 빈 딕셔너리에 {key(단어): 갯수} 형태로 집어넣기
4. 정렬하기
5. top5만 선정해서 출력하기
'''

myfile = input('파일명을 입력해주세요. 없으면 엔터:')
if myfile ==  '':
    myfile = 'crown.txt'
fhand = open(myfile)
words = []
dic = dict()
while True:
    words = fhand.readline().split()
    if not words:
        break
    for i in words:
        dic[i] = dic.get(i, 0) +1
tmp = sorted([(v, k) for (k, v) in dic.items()] , reverse = True)
print(tmp[:5])