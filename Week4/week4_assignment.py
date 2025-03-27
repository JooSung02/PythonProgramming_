number = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))
if number == 1 :
    num1 = input("수식을 입력하세요 : ")
    print(eval(num1))
elif number == 2 :
    num2_1 = int(input("첫번째 숫자를 입력하세요 :"))
    num2_2 = int(input("두번째 숫자를 입력하세요 :"))
    sum = 0
    for i in range(num2_1, num2_2 + 1) :
        sum += i
    print(num2_1, "+...+", num2_2, "의 결과는 ", sum, "입니다.")
else :
    print("잘못된 입력")