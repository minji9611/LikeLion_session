import random
PRIZE_1 = 5000000
PRIZE_2 = 100000
PRIZE_3 = 20000
PRIZE_4 = 5000


"""
#나의 첫 함수!
def get_random():
    temp = []
    while len(temp) < 6:
        a = random.randrange(1, 46)
        if a not in temp:
            temp.append(a)
    temp.sort()
    return temp
"""

nums = []
for i in range(1, 46):
    nums.append(i)


# 개선안1
# 의문 1. my_list 변수는 왜 있어야하지..?
# 아하! sort 때문에 중간다리가 필요!
def get_random2():
    my_list = random.sample(nums, 6)
    my_list.sort()
    return my_list

"""
#개선안2. my_list 제거
def get_random3():
    return random.sample(nums,6).sort()
"""

while(True):
    try:
        money = int(input("구입할 금액을 입력하세요.\n"))
    except:
        print("숫자를 다시 입력해주세요.")
    else:
        break


while money < 1000:
    money = int(input("로또의 최소 가격은 1000원입니다.\n숫자를 다시 입력해주세요.\n"))

N = money // 1000

print("> 당신은 로또", N, "개를 구매했어요")

lotto_nums = []
for i in range(N):
    lotto = get_random2()
    print(lotto)
    lotto_nums.append(lotto)

# 지난 주 당첨번호를 입력할 시에 
# 6개의 숫자가 아닐 경우 
# 로또는 6개의 숫자로 이루어집니다. 라는 문구를 출력하고 
# 입력 다시 받기

print("> 지난주 당첨 번호를 입력해주세요")
last_week = list(map(int,input().split(",")))

for i in last_week:
    if i>45 or i<1:
        print("> 1~45까지의 숫자를 입력해주세요. \n지난주 당첨 번호를 입력해주세요.")
        last_week = list(map(int,input().split(",")))  
    
while len(last_week) != 6:
    print("로또는 6개의 숫자로 이루어집니다.\n지난주 당첨 번호를 입력해주세요.")
    last_week = list(map(int,input().split(",")))


# 지난 주 당첨번호를 입력할 시에 
# 중복된 숫자를 입력할 경우 
# 중복된 숫자를 입력하실 수 없습니다. 라는 문구를 출력하고 
# 입력 다시 받기
while len(set(last_week)) != 6:
    last_week = list(map(int,input("중복된 숫자를 입력하실 수 없습니다.\n지난주 당첨 번호를 입력해주세요.\n").split(",")))


first = 0
second = 0 
third = 0
fourth = 0

for lotto_num in lotto_nums:
    count = 0
    for i in last_week:
        if i in lotto_num:
            count += 1
    if count == 6:
        first += 1
    elif count == 5:
        second += 1
    elif count == 4:
        third += 1
    elif count == 3:
        fourth += 1

print(f"> 로또 당첨 결과")
print(f"4등(3개가 맞을 때) - {PRIZE_4}원 - {fourth}개")
print(f"3등(4개가 맞을 때) - {PRIZE_3}원 - {third}개")    
print(f"2등(5개가 맞을 때) - {PRIZE_2}원 - {second}개")    
print(f"1등(6개가 맞을 때) - {PRIZE_1}원 - {first}개")    
print("> 수익률")
print((first * PRIZE_1 + second * PRIZE_2 + third * PRIZE_3 + fourth * PRIZE_4) // (N*1000))