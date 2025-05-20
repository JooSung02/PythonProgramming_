inFp = None
inList, inStr = [], ""

inFp = open(r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week10\FileTest\CookBook 파이썬을 공부합니다..txt", "r",encoding='UTF8')

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()