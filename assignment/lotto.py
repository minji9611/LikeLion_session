#https://github.com/LikeLion-CAU-9th/2week-python-lotto
import random
PRIZE_1 = 5000000
PRIZE_2 = 100000
PRIZE_3 = 20000
PRIZE_4 = 5000

def get_random():
    temp = []
    while len(temp) < 6:
        a = random.randrange(1, 46)
        if a not in temp:
            temp.append(a)
    temp.sort()
    return temp


lotto_list = []
for i in range(1, 46):
    lotto_list.append(i)


def get_random2():
    my_list = random.sample(lotto_list, 6)
    my_list.sort()
    return my_list


print("구매할 금액 입력해")
money = int(input())

N = money // 1000

print("당신은 로또", N, "개를 구매했어요")

for i in range(N):
    print(get_random2())

lastweek = input().split(,)
 answer = [int(number) for number in input("\n지난주 당첨 번호를 입력해주세요\n").split(',')]import random
PRIZE_1 = 5000000
PRIZE_2 = 100000
PRIZE_3 = 20000
PRIZE_4 = 5000

lotto_nums = []
def get_random():
    temp = []
    while len(temp) < 6:
        a = random.randrange(1, 46)
        if a not in temp:
            temp.append(a)
    temp.sort()
    return temp


nums = []
for i in range(1, 46):
    nums.append(i)


def get_random2():
    my_list = random.sample(nums, 6)
    my_list.sort()
    return my_list


def main():
    while True:
        try:
            money = int(input("구입할 금액 입력해"))
            if money < 1000:
                print("로또의 최소 가격은 1000원입니다")
            else:
                break
        except:
            print("숫자를 입력해주세요")


N = money // 1000

print("> 당신은 로또", N, "개를 구매했어요")

for i in range(N):
    lotto = get_random2()
    print(lotto)
    lotto_nums.append(lotto)

print("> 지난주 당첨 번호를 입력해주세요")
last_week = list(map(int,input().split(",")))

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
print("> 로또 당첨 결과")
print(f"4등(3개가 맞을 때) - {PRIZE_4}원 - {fourth}개")    
print(f"3등(4개가 맞을 때) - {PRIZE_3}원 - {third}개")    
print(f"2등(5개가 맞을 때) - {PRIZE_2}원 - {second}개")    
print(f"1등(6개가 맞을 때) - {PRIZE_1}원 - {first}개")    
print("> 수익률")
print(first * PRIZE_1 + second * PRIZE_2 + third * PRIZE_3 + fourth * PRIZE_4 / (N*1000))