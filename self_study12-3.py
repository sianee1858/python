import threading

def cal_sum(name, limit):
    total = 0
    for i in range(1, limit +1):
        total +=1
    print(f"{name} = {total}")

t1 = threading.Thread(target=cal_sum, args=("1+2+...+1000"))
t2 = threading.Thread(target=cal_sum, args=("1+2+...+10000"))
t3 = threading.Thread(target=cal_sum, args=("1+2+...+100000"))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()