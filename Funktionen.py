def multi_print(name, count):
    for i in range(0, count):
        print(name)

def multi_print2(name, count):
    vS_String = ""
    for i in range(0, count):
        vS_String = vS_String + name + " "
    return vS_String    

def start_Function():
    multi_print("Daniel", 10)
    multi_print("Wolf", 10)
    print(multi_print2("Daniel", 5))

start_Function()