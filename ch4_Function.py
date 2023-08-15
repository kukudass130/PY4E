def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours >40:
        print("초과 근무입니다!")
        rep = 40 * rate
        otp = (hours -40.0) * (rate *1.5)
        pay = rep + otp
    else:
        print("정규 근무 시간입니다.")
        pay = hours * rate
    print("Returning", pay)
    return pay

# 근무시간과 시급을 입력하면 임금총액을 계산해주는 프로그램
hours = float(input('총 근무시간을 입력해주세요: '))
rate = float(input('시급을 입력해주세요: '))

money = computepay(hours, rate)
print('임금 총액: ', money)