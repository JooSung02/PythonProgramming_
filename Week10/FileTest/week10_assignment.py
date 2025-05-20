inFp = None
inStr = ""
i = 1
inFp = open(r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week10\FileTest\CookBook 파이썬을 공부합니다..txt", "r",encoding='UTF8')

while True :
    print(i,"\b: ", end="")
    inStr = inFp.readline()
    i += 1
    if inStr == "" :
        break
    print(inStr, end="")

inFp.close()