fhand = open('mbox_short.txt')

#직접 혼자 짜본 코드
'''
for i in fhand:
    i = i.rstrip()
    if len(i) > 0:
        char_list = i.split()
        if char_list[0] == 'From':
            print(f'email: {char_list[1]}')
'''

#guardian code 활용
for i in fhand:
    i = i.strip()
    char_list = i.split()
    #guardian(18~19) : 이메일이 없는 from만 있는 부분은 넘어간다.
    if len(char_list) <2:
        continue
    if char_list[0] == 'From':
        print(f'email: {char_list[1]}')