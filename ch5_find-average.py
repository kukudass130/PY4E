list1 = list(map(int, input().split()))
#리스트에서 요소 개수구하기{len(리스트명)}
'''
    print(len(list1))
    >>>요소의 개수
'''
#리스트에서 특정 요소의 개수 구하기{리스트명.count()}
'''
    value = [1, 2, 3, 3, 4 ,5]
    print(value.count(3))
    >>>2
'''
count = 0
total = 0
for value in list1:
    count = count +1
    total = total + value
    print(f'현재 수: {value}, 갯수:{count}, 합계:{total}')
aver = total /count
print(f'원소의 총 개수와 합계는 {count}, {total}이고\n 평균은 {aver:.4f}입니다.')
#소수점 관리 방법 
#1. round(반올림하는 값, 자릿수)
#2. f-string에서 {변수: 0.nf} //n은 소수점 자릿수. 예제에서 사용.
#3. format 서식 지정 "[출력할 문자열] {:.nf}".format(값1, 값2) //n은 소수점 자리수
