import os
import pandas as pd
#mit pandas kann man z.B. eine CSV Datei einlesen

def main():
    pathToFile = pathFolderJoiner()

    #gibt die Datei in einem zurück
    #print(pd.read_csv(pathToFile, delimiter=";"))

    df = pd.read_csv(pathToFile, delimiter=";")
    
    #method1(df)
    #method2(df)
    #method3(df)
    method4(df)
    

def method1(df):
    print(len(df))
    #Ausgabe: 3 Datensätze

    print(df["Name"])
    #gibt die Werte in einer Spalte aus
    for name in df["Name"]:
        print(name)

    #gibt den Werte in der Zeile mit dem Index 1 zurück
    print(df.iloc[1])

def method2(df):
    #Zeile für Zeile durchlaufen
    #Liefert ein Tupel zurück, an erster Stelle steht der Index. An zweiter Stelle der eigentliche Tabelleninhalt
    for row in df.iterrows():
        print(row)
        break

def method3(df):
    #hierbei wird das Tupel entpackt und in die Variablen pos (mit dem Index) und d (mit dem eigentlichen Tabelleninhalt) gespeichert
    for row in df.iterrows():
        #Tupel = (0,1) => (Index, Tabelleninhalt) => pos, d
        pos, d = row
        print(pos)
        print(d)
        break

def method4(df):
    #Damit filtert man das Dataframe und ich bekomme alle Datensätze zurück, bei denen Mannheim drin steht
    df = df[df["Stadt"] == "Mannheim"]
    print (df)



def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training', 'TestFile.csv')


main()