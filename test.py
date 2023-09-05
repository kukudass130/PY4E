myfile = input('파일명을 입력해주세요. 없으면 엔터:')
if myfile ==  '':
    myfile = 'crown.txt'
fhand = open(myfile)
words = []
print(fhand.readline().split())