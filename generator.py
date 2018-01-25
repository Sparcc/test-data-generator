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
            self.parseRow
            #print(row)
            writer.writerow(row)
            i+=1            
        ofile.close()
        
    def parseRow(self):
        self.randomiseFields(row,(1,999))
        
    def randomiseField(self, row, field, range):
        row[fieldsToRand[field]]=random.randint(range)
        
    def randomiseFields(self, row, range):
        for value in fieldsToRand:
            row[fieldsToRand] = random.randint(range)
        
    def calculateField(self, row, *field):
        #add your own algorithm here
        row[fieldsToRand[field[2]]] = row[fieldsToRand[field[0]]] + row[fieldsToRand[field[1]]]