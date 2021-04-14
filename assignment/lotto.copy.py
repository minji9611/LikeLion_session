import random

LOTTO_PRICE = 1000
SMALLEST_LOTTO_NUMBER = 1
LARGEST_LOTTO_NUMBER = 45
PRIZE_1 = 5000000
PRIZE_2 = 100000
PRIZE_3 = 20000
PRIZE_4 = 5000


def get_affordable_lotto(price):
    return price // LOTTO_PRICE


def print_affordable_lotto(price):
    affordable_number = get_affordable_lotto(price)
    print(affordable_number, "장의 로또를 구입하셨습니다.")


def get_random_lotto_number():
    return random.randint(SMALLEST_LOTTO_NUMBER, LARGEST_LOTTO_NUMBER)


def lotto_generator(sheets):
    result = []
    sheet = []
    for i in range(0, sheets):
        for k in range(0, 6):
            while True:
                new_number = get_random_lotto_number()
                if new_number not in sheet:
                    sheet.append(new_number)
                    break
        sheet.sort()
        result.append(sheet)
        sheet = []
    return result


def print_and_return_purchased_lotto(sheets):
    sheet = lotto_generator(sheets)
    for i in range(0, len(sheet)):
        print(sheet[i])
    return sheet


def get_score_index(sheet, answer):
    sheet_index = 0
    answer_index = 0
    score = 0
    while True:
        if sheet_index >= 6 or answer_index >= 6:
            break
        if sheet[sheet_index] == answer[answer_index]:
            score += 1
            sheet_index += 1
            answer_index += 1

        elif sheet[sheet_index] < answer[answer_index]:
            sheet_index += 1
        else:
            answer_index += 1
    if score == 3:  # 3개를 맞추면
        return 3  # 4등이고, 4등의 개수는 3번 index
    elif score == 4:  # 4개를 맞추면 3등
        return 2
    elif score == 5:  # 5개를 맞추면 2등
        return 1
    elif score == 6:  # 6개를 맞추면 1등
        return 0
    else:  # 1 ~ 4등이 아닐 경우
        return -1


def get_score_list(purchased, answer):
    score_list = [0, 0, 0, 0]  # 0번 index부터 1등, ... , 4등 lotto 개수
    for i in range(0, len(purchased)):
        score_index = get_score_index(purchased[i], answer)
        if score_index != -1:
            score_list[score_index] += 1
    return score_list


def print_lotto_result(purchased, answer):
    score_list = get_score_list(purchased, answer)
    print("4등(3개가 맞을 때) - 5000원 -", score_list[3])
    print("3등(4개가 맞을 때) - 20000원 -", score_list[2])
    print("2등(5개가 맞을 때) - 100000원 -", score_list[1])
    print("1등(6개가 맞을 때) - 5000000원 -", score_list[0])


def get_benefit(score_list):
    benefit = 0
    for i in range(0, 4):
        if i == 0:  # 1등
            benefit += score_list[i] * PRIZE_1
        elif i == 1:  # 2등
            benefit += score_list[i] * PRIZE_2
        elif i == 2:  # 3등
            benefit += score_list[i] * PRIZE_3
        elif i == 3:  # 4등
            benefit += score_list[i] * PRIZE_3
    return benefit


def check_valid_range(answer):
    for i in range(0, len(answer)):
        if answer[i] < 1 or answer[i] > 45:
            return False
    return True


def check_repetition(answer):  # 반복되는 값이 있으면 False return
    for i in range(0, len(answer)):
        for k in range(i + 1, len(answer)):
            if answer[i] == answer[k]:
                return False
    return True


def main():
    while True:
        try:
            price = int(input("\n구입금액을 입력해 주세요.\n"))
            if price < 1000:
                print("로또의 최소 가격은 1000원입니다")
            else:
                break
        except:
            print("숫자를 입력해주세요")
    print_affordable_lotto(price)
    purchased_lotto = print_and_return_purchased_lotto(get_affordable_lotto(price))
    while True:
        try:
            answer = [int(number) for number in input("\n지난주 당첨 번호를 입력해주세요\n").split(',')]
            if len(answer) != 6:
                print("로또는 6개의 숫자로 이루어집니다.")
            else:
                if check_valid_range(answer):
                    if check_repetition(answer):
                        break
                    else:
                        print("중복된 숫자를 입력하실 수 없습니다.")
                else:
                    print("1~45까지의 숫자를 입력해주세요")
        except:
            print("숫자를 입력해주세요")

    score_list = get_score_list(purchased_lotto, answer)
    print("\n********** 로또 결과 **********")
    print_lotto_result(purchased_lotto, answer)
    benefit = get_benefit(score_list) / price
    print("\n수익률\n", round(benefit, 2), "배")


if __name__ == "__main__":
    main()