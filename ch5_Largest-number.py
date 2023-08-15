list1 = list(map(int, input().split()))
#input().split()까지 사용했을 때는 여러 원소를 char로 입력받음.
#map까지만 사용했을 때는 각 원소의 타입(int, float, double...)을 지정.
#list 키워드를 사용해 입력받은 원소들을 하나의 리스트로 묶음.
def find_large(list1):
    largest_so_far = -1
    for the_num in list1:
        if the_num >largest_so_far:
            largest_so_far = the_num
        print(largest_so_far, the_num)
    return largest_so_far
max_num= find_large(list1)
print(f'가장 큰 숫자는 {max_num}입니다.')