for i in range(2, 10) :
    print("# ", i, "단 #  ", end='')

print("\n")

for j in range(2, 10) :
    for k in range(2, 10) :
        print(k,"\bX",j, "=",k*j,"  ", end='')
    print("\n")