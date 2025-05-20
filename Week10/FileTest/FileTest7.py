outFp = None
outStr = ""

outFp = open(r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week10\FileTest\data2.txt", "w")

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break

outFp.close()
print("--정상적으로 파일에 씀 ---")