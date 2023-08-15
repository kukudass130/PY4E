# 터미널에서 파이썬 파일을 실행하는법.
"""
    1. dir //현재 경로 확인. (맥은 pwd)
    2. cd 실행할 파일 폴더 경로 //실행할 파일이 위치한 폴더로 이동. 
    3. python "파일명.py" //파일 실행
    tip) cls명령어로 cmd를 깔끔하게 지울 수 있다! (맥은 command +k)
"""
# 이름을 입력받아 환영인사와 함께 출력하기 
nzt = input('Enter your name: ')
print('Welcome', nzt)

# 근무시간과 시급을 입력하면 임금총액을 계산해주는 프로그램
hour = float(input('총 근무시간을 입력해주세요: '))
rph = float(input('시급을 입력해주세요: '))
money = hour * rph
print('임금 총액은', str(money) + '원 입니다.')
    #변수 money(type == flaot)를 문자열로 바꾸지 않고
    #다른 문자열과 +연산자를 사용하면 오류가 발생!