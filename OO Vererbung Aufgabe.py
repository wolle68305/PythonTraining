class FileReader():
    def __init__(self, fileName):
        self.fileName = fileName
    def lines(self):
        lines = []
        with open(self.fileName, "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines
    

class CSVReader(FileReader):
    def __init__(self, fileName):
        super().__init__(fileName)
    def lines(self):
        lines = super().lines()

        
        #kürzere Variante
        return[line.split(",") for line in lines]
        
        #längere Variante
        #lines_splitted = []
        #for line in lines:
        #    lines_splitted.append(line.split(","))
        #return lines_splitted    

#f = FileReader("/home/daniel/Dokumente/Python Training/datei.csv")
f = CSVReader("/home/daniel/Dokumente/Python Training/datei.csv")
print(f.lines())


