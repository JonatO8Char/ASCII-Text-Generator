from inspect import getfullargspec
class Letter:
    def __init__(self, row):
        self.arrayRow = []
        self.arrayRow.append(row[0])
        self.arrayRow.append(row[1])
        self.arrayRow.append(row[2])
        self.arrayRow.append(row[3])
        self.arrayRow.append(row[4])
        self.arrayRow.append(row[5])
        self.arrayRow.append(row[6])


    
    def printRow(self, rowNum):
        print(self.arrayRow[rowNum].strip('\n'), end = " ")
    
    def __str__(self) -> str:
        s = ""
        for i in self.arrayRow:
            s += i
        return s

    
