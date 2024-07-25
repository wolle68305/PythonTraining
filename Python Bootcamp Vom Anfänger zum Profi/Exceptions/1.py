def main():
     #method1()
     #method2()
     #method3()
     method4()

def method1():
    try:
        print(5/0)
        print(4)
    except ZeroDivisionError:
            print("Durch null teilen ist nicht erlaubt")
    print(5)

def method2():
     try:
          with open("datei.xyz", "r") as file:
               print(file)
     except FileNotFoundError:
          print("Datei nicht gefunden")          

def method3():
    #mehrere Exceptions in einer Methode
    try:
        with open("datei.xyz", "r") as file:
            print(file)
        print(5/0)
    except FileNotFoundError:
          print("Datei nicht gefunden") 
    except ZeroDivisionError:
            print("Durch null teilen ist nicht erlaubt")


def method4():
     try:
          method4Teil2()
     except ZeroDivisionError:
          print("Du darfst nicht durch null teilen")

def method4Teil2():
     print(5/0)

main()    