import os
def main():
    pathToFile = "/home/daniel/TransferSynology/Python Training/gaeste.txt"
    method1(pathToFile)
    #method2(pathToFile)
    #getCurrentFolderLocation()

def method1(pathToFile):
    f = open(pathToFile , "r")
    print(f.read())

def method2(pathToFile):
    with open(pathToFile, 'r', encoding='utf-8') as file:
        print(file)

def getCurrentFolderLocation():
    print(os.getcwd())

main()