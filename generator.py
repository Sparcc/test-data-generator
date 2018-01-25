import csv
import random

class settings:
    ofile  = open('output.csv', "w", newline='')
    writer = csv.writer(ofile)
    fields = ["Num1","Op","Num2","Result"]
    fieldsToRand = {"Num1":0, "Num2":2}
    writer.writerow(fields)
    
    def settings(lines = 15):
        self.linesOfData = lines
        
class generator:
    def generator(self, settings)
        self.settings = settings
        
    def generateDataCSV(self):
        i = 0
        while i < self.settings.linesOfData: 
            row = self.settings.fields
            row[0] = random.randint(1,99)
            row[2] = random.randint(1,99)
            opNum = random.randint(0,3)
            if opNum == 0:
                row[1] = "plus"
                row[3] = row[0] + row[2]
            if opNum == 1:
                row[1] = "minus"
                row[3] = row[0] - row[2]
            if opNum == 2:
                row[1] = "times"
                row[3] = row[0] * row[2]
            if opNum == 3:
                row[1] = "divide"
                if row[0] == 0:
                    row[0] = random.randint(1,99)
                if row[2] == 0:
                    row[2] = random.randint(1,99)
                row[3] = row[0] / row[2]
            #print(row)
            writer.writerow(row)
            i+=1
        ofile.close()
    def parseRow(self):
        print(stub)
        
    def randomiseField(self, row, field, range, format)
        
    def randomiseFields(self, row, range, format):
        for value in row:
            if value
            random.randint(range)
        print(stub)
        
    def calculateField(self, row, field):
        print(stub)