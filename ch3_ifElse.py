# 근무시간과 시급을 입력하면 임금총액을 계산해주는 프로그램
hour = float(input('총 근무시간을 입력해주세요: '))
rph = float(input('시급을 입력해주세요: '))
if hour >40:
    print("초과 근무입니다!")
    rep = 40 * rph
    otp = (hour -40.0) * (rph *1.5)
    money = rep + otp

else:
    print("정규 근무 시간입니다.")
    money = hour * rph
print('임금 총액은', str(money) + '원 입니다.')