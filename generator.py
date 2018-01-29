import csv
import random
import sys,os
import time
sys.path.append(os.getcwd())

class Settings:
    ofile  = open('output.csv', "w", newline='')
    writer = csv.writer(ofile)
    fields = ["Num1","Op","Num2","Result"]
    fieldsToRand = {"Num1":0, "Num2":2}
    linesOfData = 15
    
    def __init__(self, lines = 15):
        self.linesOfData = lines
        self.writer.writerow(self.fields)
        
class Generator:
    def __init__(self, settings):
        self.settings = settings
        
    def generateDataCSV(self):
        print("Generating...")
        start = time.time()
        i = 0
        while i < self.settings.linesOfData: 
            row = list(self.settings.fields)
            self.parseRow(row)
            self.settings.writer.writerow(row)
            i+=1
        self.settings.ofile.close()
        end = time.time()
        print("Done! - Finished in: %.2f seconds" % float(end-start))
    
    #customisable
    def parseRow(self, row):
        self.randomiseFields(row,999)
        self.calculateField(row, "Num1", "Op", "Num2", "Result")
        #self.calculateField(row, "All", allFields = True)
    
    def randomiseField(self, row, field, upperRange):
        row[fieldsToRand[field]]=random.randint(1,upperRange)
        
    def randomiseFields(self, row, upperRange):
        for value in self.settings.fieldsToRand:
            row[self.settings.fieldsToRand[value]] = random.randint(1,upperRange)
    
    #customisable
    def calculateField(self, row, *fields, allFields = False):
        if allFields == True:
            fields = list(self.settings.fields)
        #add your own algorithm here
        result = 0
        op = random.randint(0,3)
        if op == 0:
            result = \
            row[self.settings.fields.index(fields[0])] + row[self.settings.fields.index(fields[2])]
            row[self.settings.fields.index(fields[1])] = "plus"
        if op == 1:
            result = \
            row[self.settings.fields.index(fields[0])] - row[self.settings.fields.index(fields[2])]
            row[self.settings.fields.index(fields[1])] = "minus"
        if op == 2:
            result = \
            row[self.settings.fields.index(fields[0])] / row[self.settings.fields.index(fields[2])]
            row[self.settings.fields.index(fields[1])] = "divide"
        if op == 3:
            result = \
            row[self.settings.fields.index(fields[0])] * row[self.settings.fields.index(fields[2])]
            row[self.settings.fields.index(fields[1])] = "minus"
        
        row[self.settings.fields.index(fields[(len(fields)-1)])] = result