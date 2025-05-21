import threading

def calculate_sum(n) :
    total = n*(n+1) // 2
    print("1+2+3+...... +", n, "= %d" %total)

th1 = threading.Thread(target=calculate_sum(1000))
th2 = threading.Thread(target=calculate_sum(10000))
th3 = threading.Thread(target=calculate_sum(100000))