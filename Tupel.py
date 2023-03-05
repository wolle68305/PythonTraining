#Tupel ist eine unveränderliche Datenstruktur

def main():
    vTupel = ()
    vTupel = create_Tupel(vTupel)

    print(vTupel)
    print(vTupel,0)

def create_Tupel(affectedTupel):
    affectedTupel = (1,2,3)
    return affectedTupel

def return_SingleValueFormTupel(affectedTupel, positionOfReturnValue):
    return affectedTupel[positionOfReturnValue]

main()