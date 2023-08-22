'''
Q2. 한 중학교에서는 중간고사가 끝난 후, 학생들의 시험 답지와 정답지를 비교하여 점수를 계산하는 채점 프로그램을 도입하려고 합니다.
 학생들의 시험 답지와 정답지가 다음과 같이 주어졌을 때, 파이썬 함수를 활용하여 다음의 요구사항을 충족하는 채점 프로그램을 만들어보세요.

<요구사항>

1. 학생들의 답안을 채점해주세요.
2. 모든 학생들의 점수를 계산하고 등수를 매겨주세요.
3. 최종적으로 학생들의 점수와 등수를 출력하세요.

# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
alist = [3,2,4,2,5,2,4,3,1,2]


✔︎ 보조 설명 :

총 10문제로 구성
학생들의 답안과 정답지를 비교하여 점수를 계산하고, 각 학생의 점수와 등수를 출력

학생들의 답안은 's' 리스트에 이름과 답안 문자열로 주어졌습니다.
이름과 답안은 쉼표(,)로 구분되어 있습니다. 예를 들어 "김갑" 학생의 답안은 "3242524215" 입니다.
정답은 'alist' 리스트로 주어지며, 각 문제에 대한 정답은 숫자로 나타내어져 있습니다.

1. 학생들의 답안과 정답을 각 변수에 문자열의 형태로 저장합니다.
2. 채점 함수를 만듭니다.
   - 채점 함수는 학생의 답안과 정답을 비교하여 점수를 계산합니다.
   - 각 문제에 대해 학생의 답안과 정답을 비교해, 일치하면 해당 문제의 점수를 학생의 총점에 더합니다.
   - 모든 문제를 채점한 후, 학생별 총 점수를 반환합니다.
3. 모든 학생들의 점수 계산을 완료한 후, 등수를 매깁니다.
   - 학생들의 점수와 이름을 쌍으로 묶은 리스트를 생성합니다.
   - 리스트를 점수 기준으로 내림차순으로 정렬합니다.
4. 최종적으로 학생들의 점수와 등수를 출력합니다.
'''
def input_data():
    S = []
    while True:
        try:
            name , answer = input('학생 이름과 답안을 입력하세요:').split()
        except:
            name = None
        if name == None:
            break
        S.append(f'{name},{answer}')
    return S
def check(data_list , alist):
    check_list = []
    for i in range(len(data_list)):
        score = 0
        startpoint = data_list[i].find(',')
        answer = data_list[i]
        answer_list = list(answer[startpoint+1:])   #숫자만 가져와 답안준비 완.
        #답안 비교 루프
        for j in range(len(alist)):
            if answer_list[j] == alist[j]:
                score = score +1
        check_list. append(f'{score}점: {answer[:startpoint]}')
        check_list.sort(reverse=True)
    return check_list

a = ['3','2','4','2','5','2','4','3','1','2']
s = input_data()    #학생 자료 입력 함수까지 완.
result = check(s , a)
print(result)