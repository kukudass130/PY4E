#문제 설명
'''
Q4. 한 IT 기업에서는 신규 직원의 신상정보를 확인하는 시스템을 도입하려고 합니다.
 이 시스템은 주민등록번호를 받아 해당 직원이 몇년 몇월에 태어났는지 그리고 남자인지 여자인지를 출력하는 기능을 제공합니다.
 파이썬을 활용해 다음의 조건을 충족하는 프로그램을 만들고, 효율적인 인사 관리 시스템을 만들어보세요. [난이도 : ⭐️⭐️⭐️⭐️/5]

주민등록번호는 6자리 이후에 '-'로 구분되어야 하며,
 총 길이는 '-'를 포함하여 14자리임 주민등록번호의 뒷자리 시작번호가 1 또는 3인 경우 해당 직원은 남성, 2 또는 4인 경우 해당 직원은 여성임
 주민등록번호의 뒷자리 3, 4를 가질 수 있는 경우는 2000년생 이후 출생자 뿐임 주어진 주민등록번호가 조건을 만족하지 않을 경우, "잘못된 번호입니다"라는 메세지를 출력함

✔︎ 보조 설명 : 주민등록번호는 우리나라에서 사용하는 신분증 번호로, 생년월일과 성별 정보가 포함되어 있습니다. 
 이 문제에서는 주민번호를 입력하면 해당 개인이 언제 태어났는지, 그리고 남성인지 여성인지를 출력하는 함수를 만들어보려고 합니다.

이 문제를 해결하기 위해서는 입력된 주민등록번호를 분석하여 생년월일과 성별을 정확히 판별하는 함수를 작성해야합니다.
 조건을 하나씩 확인하면서 주민등록번호의 유효성을 검사하고, 결과를 출력하는 로직을 구현해보세요.

구현 순서
1. 사용자로부터 주민등록번호를 입력받습니다.
2. 입력된 주민등록번호의 길이와 형식을 확인합니다.
    만약 길이와 형식이 맞지 않을 경우, "잘못된 번호입니다" 메세지를 출력하고 프로그램을 종료합니다.
3. 주민등록번호의 뒷자리 시작번호를 확인하여 성별을 판별합니다.
4. 주민등록번호의 앞 2자리가 00부터 23까지인 경우, 출생년도 확인이 필요합니다.
    이 경우 사용자에게 "2000년 이후 출생자입니까? (O/X)"와 같은 질문을 출력합니다.
    사용자의 입력을 받아 맞으면 "20##"년생, 틀리면 "19##"년생으로 저장합니다.
5. 최종적으로 생년월일과 성별을 출력합니다.
'''
#올바른 형식 판별
def form_func(numlist_f):
    if len(numlist_f) != 14 or numlist_f[6] != '-':
        print('잘못된 번호입니다.')
        exit()
#성별 판별
def gender_func(numlist_g):
    gend = None
    print(numlist_g[7])
    if numlist_g[7] == '1' or numlist_g[7] == '3':
        print('남성')
        gend = '남성'
    elif numlist_g[7] == '2' or numlist_g[7] == '4':
        print('여성')
        gend = '여성'
    else:
        print('잘못된 번호입니다.')
    return gend
#생년월일 판별
def birth_func(numlist_b):
    first_bir = int(numlist_b[0]+numlist_b[1])
    bir = None
    if first_bir in range(0, 24):
        ps = input('2000년 이후 출생자입니까? (O/X)')
        if ps == 'O' or ps == 'o':
            bir = 2000 + first_bir
        elif ps == 'X' or ps == 'x':
            bir = 1900 + first_bir
    return bir

person_num =list(input('-을 포합하여 주민등록번호를 입력하세요(6자리-7자리): '))
form_func(person_num)
gender = gender_func(person_num)
birthday = birth_func(person_num)
print(f'생년월일: {birthday}년 {person_num[2]+person_num[3]}월 {person_num[4]+person_num[5]}일\n셩별: {gender}')