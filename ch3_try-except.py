# cmd에서 cd ..을 이용하여 상위 폴더로 위치 변경가능.
# 근무시간과 시급을 입력하면 임금총액을 계산해주는 프로그램
hr = input('총 근무시간을 입력해주세요: ')
pay = input('시급을 입력해주세요: ')
try:
    hour = float(hr)
    rph = float(pay)
#예외 상황(값이 숫자가 아닐 때)이 발생하면 프로그램을 멈춘다.
except:
    print("Error, 숫자를 입력해주세요!")
    quit()
    #quit()를 이용하여 프로그램을 강제로 종료시킬 수 있다.
if hour >40:
    print("초과 근무입니다!")
    rep = 40 * rph
    otp = (hour -40.0) * (rph *1.5)
    money = rep + otp

else:
    print("정규 근무 시간입니다.")
    money = hour * rph
print('임금 총액은', str(money) + '원 입니다.')