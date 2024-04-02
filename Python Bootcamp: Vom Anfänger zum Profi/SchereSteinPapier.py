import random

def main():
    vBol_NeueRunde = True
    vS_InputString = ""    

    while vBol_NeueRunde == True:
        vI_RandomNumber = random.randint(0,2)
        
        if(vI_RandomNumber == 0):
            vS_RandomValue = "Schere"
        elif(vI_RandomNumber == 1):
            vS_RandomValue = "Stein"
        elif(vI_RandomNumber == 2):
            vS_RandomValue = "Papier"

        vS_InputChoice = input("Schere, Stein oder Papier ? (Schere, Stein, Papier)")        
        
        if(vS_InputChoice == "Schere" and vS_RandomValue == "Schere"):
           vS_Result = "Unentschieden"
        elif(vS_InputChoice == "Schere" and vS_RandomValue == "Stein"):
           vS_Result = "Verloren"
        elif(vS_InputChoice == "Schere" and vS_RandomValue == "Papier"):
           vS_Result = "Gewonnen"
        elif(vS_InputChoice == "Stein" and vS_RandomValue == "Schere"):
           vS_Result = "Gewonnen"
        elif(vS_InputChoice == "Stein" and vS_RandomValue == "Stein"):
           vS_Result = "Unentschieden"                 
        elif(vS_InputChoice == "Stein" and vS_RandomValue == "Papier"):
           vS_Result = "Verloren"
        elif(vS_InputChoice == "Papier" and vS_RandomValue == "Schere"):
           vS_Result = "Verloren"      
        elif(vS_InputChoice == "Papier" and vS_RandomValue == "Stein"):
           vS_Result = "Gewonnen"
        elif(vS_InputChoice == "Papier" and vS_RandomValue == "Papier"):
           vS_Result = "Unentschieden"


        print("Das Ergebnis lautet: " + vS_Result + ". Der Computer hat " + vS_RandomValue + " gewählt")

        vS_InputString = input("Neue Runde ? (Y/N)")

        if(vS_InputString == "Y"):
            vBol_NeueRunde = True
        elif(vS_InputString == "N"):
            vBol_NeueRunde = False    


main()