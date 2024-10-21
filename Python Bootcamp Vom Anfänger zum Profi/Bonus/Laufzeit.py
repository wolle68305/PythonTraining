from datetime import datetime

def method1():
    start = datetime.now()
    s = 0
    for i in range(0,100000000):
        s = s + 1
    print(s)
    end = datetime.now()
    print(end-start)


method1()




