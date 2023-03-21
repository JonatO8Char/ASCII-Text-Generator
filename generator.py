from Letter import Letter

class Generator:
    def __init__(self):
        self.alphabet = []
    
    def createAscii(self, fileName):
        with open(fileName, encoding='utf8') as f:
            row = 0
            lineRow = [[]for i in range(7)]
            for line in f:
                if line != '\n':
                    lineRow[row] = line
                    if row == 6:
                        letter = Letter(lineRow)
                        self.alphabet.append(letter)
                    row = (row + 1) % 7
    
    def printString(self, message):
        message = message.lower()

        for row in range(7):
            for letter in message:
                if letter != " ":
                    self.alphabet[ ord(letter) - ord('a')].printRow(row)
                else:
                    self.alphabet[-1].printRow(row)
            print()

# test run
generator = Generator()
generator.createAscii('style.txt')
generator.printString('total completion')







