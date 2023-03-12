def main():
    functionChoice = input("Welche Funktion soll ausgeführt werden: ")

    if int(functionChoice) == 1:
        function1()

    if int(functionChoice) == 2:
        function2()

    if int(functionChoice) == 3:
        function3()

    if int(functionChoice) == 4:
        function4()

    if int(functionChoice) == 5:
        function5()    

def function1():
    #gibt den Typ von "Hallo Welt" zurück
    print(type("Hallo Welt"))
    
    #gibt den Typ von 26 zurück
    print(type(26))


def function2():
    two_digit_number = input("Type a two digit number: ")

    if two_digit_number != "" and isinstance(two_digit_number,int):
        first_digit = two_digit_number[0]
        second_digit = two_digit_number[1]

        print(first_digit)
        print(second_digit)

def function3():
    number1 = input("Type number 1: ")
    number2 = input("Type number 2: ")        


    if number1 != "" and number2 != "":
        #gibt eine Float Zahl zurück
        print(int(number1)/int(number2))
        
        #gibt eine ganze Zahl zurück, rundet dabei ab
        print(int(number1)//int(number2))

        number3 = int(number1)/int(number2)
        #teilt number3 durch 2 und speichert den Wert in number3
        number3 /= 2
        print(number3)

def function4():
    #f-String
    #einfache Möglichkeit verschiedene Datentypen schnell zusammenzuführen
    score = 0
    height = 1.8
    isWinning = True

    print(f"your score is {score}, your height is {height} and your winning is {isWinning}")

def function5():
    #Exercise Tip Calculator
    totalBillSum = input("What was the total bill?")
    tipPercentage = input("What percentage tip would you like to give ? 10, 12 or 15 ?")
    sumOfPeople = input("How many people to split the bill ?")

    if totalBillSum.find("€") > 0:
        totalBillSum = totalBillSum.replace("€","")

    if totalBillSum.find(",") > 0:
        totalBillSum = totalBillSum.replace(",",".")    

    if totalBillSum.find(" ") > 0:
        totalBillSum = totalBillSum.replace(" ","")                                  


    if tipPercentage.find("%") > 0:
        tipPercentage = tipPercentage.replace("%","")

    if tipPercentage.find(" ") > 0:
        tipPercentage = tipPercentage.replace(" ","")

    sumPlusPercentage = float(totalBillSum) + ((float(totalBillSum) / 100) * int(tipPercentage))   

    endSumEachPeople = float(sumPlusPercentage) / int(sumOfPeople)

    endSumEachPeople = round(endSumEachPeople,2)

    print(f"Each person schould pay: {endSumEachPeople}€")
main()