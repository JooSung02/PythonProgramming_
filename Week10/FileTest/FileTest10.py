inFp, outFp = None, None
inStr = ""

inFp = open("C:\\Windows\\win.ini", "rb")
outFp = open(r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week10\FileTest\data2.txt", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("---이진 파일이 정상적으로 복사되었음.---")