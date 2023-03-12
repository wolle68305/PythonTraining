def main():
    woerter ={}
    woerter2 = {}
    single_Word = ""
    woerter = create_Dict(woerter)
    #printout_CompleteDict(woerter)
    
    #print(return_SingleWord(woerter,"house"))
    #print(checkIfWordIsInDict(woerter,"hous"))
    #woerter2 = (copyDict(woerter, woerter2))
    #print(woerter2)
    #print(clearDict(woerter))
    #print(updateDict(woerter2, "name", "Mizi"))
    
    delKeyAndValueFromDict("cat", woerter)

    iterateAndPrintKeyFromDict(woerter)
    iterateAndPrintValueFromDict(woerter)
    iterateAndPrintKeyAndValueFromDict(woerter)

def create_Dict(affected_Dict):
    affected_Dict = {"house" : "Haus", "cat" : "Katze", "black" : "Schwarz"}
    return(affected_Dict)

def printout_CompleteDict(affected_Dict):
    print(affected_Dict)

def return_SingleWord(affected_Dict, vS_Key):
    # affected_Dict.Get(vS_Key) liefert das gleiche zurück, wenn der Key nicht gefunden wird kommt hier ein "none" zurück
    # wenn bei der eckigen Schreibweise der Key nicht gefunden wird, dann bricht das Programm hart ab mit einer Fehlermeldung
    return affected_Dict[vS_Key]

def checkIfWordIsInDict(affected_Dict, vS_Key):
    if vS_Key in affected_Dict :
        return True
    else:
        return False    

def copyDict(affected_Dict, affected_Dict2):
    affected_Dict2 = affected_Dict.copy()
    return affected_Dict2

def clearDict(affected_Dict):
    affected_Dict.clear()
    return affected_Dict

def updateDict(affected_Dict,vS_Key, vS_Value):
    #Ausgabe "{'house': 'Haus', 'cat': 'Katze', 'black': 'Schwarz', 'name': 'Mizi'}"
    vD_updateDict = {vS_Key : vS_Value}
    affected_Dict.update(vD_updateDict)
    return affected_Dict

def iterateAndPrintKeyFromDict(affected_Dict):
    #Ausgabe "house, cat, black"
    for key in affected_Dict.keys():
        print(key)

def iterateAndPrintValueFromDict(affected_Dict):
    #Ausgabe "Haus, Katze, Schwarz"
    for key in affected_Dict.values():
        print(key)

def delKeyAndValueFromDict(affectedKey, affected_Dict):
    del affected_Dict[affectedKey]

def iterateAndPrintKeyAndValueFromDict(affected_Dict):
    for key, value in affected_Dict.items():
        print(key + ":" + value)

main()