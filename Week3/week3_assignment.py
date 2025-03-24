i = input("입력 진수 결정(16/10/8/2) : ")
n = input("값 입력 : ")
n = int(n, int(i))

print("16진수 ==> ", hex(n))
print("10진수 ==> ", n) 
print("8진수 ==> ", oct(n))
print("2진수 ==> ", bin(n))