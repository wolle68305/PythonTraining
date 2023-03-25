def multi_print(name, count):
    for i in range(0, count):
        print(name)

def multi_print2(name, count):
    vS_String = ""
    for i in range(0, count):
        vS_String = vS_String + name + " "
    return vS_String    

def function2(name="Max Mustermann",count=1):
    #Funktion mit Default Werten, d.h. wenn Parameter name und count keinen Wert übergeben bekommen, dann verwenden die Variablen den Default Wert hinter dem "=" Zeichen
    print("Name: " + name + " Count: " + str(count))

def start_Function():
    multi_print("Daniel", 10)
    multi_print("Wolf Test", 10)
    print(multi_print2("Daniel", 5))
    function2()
    function2("Daniel Wolf", 10)

start_Function()