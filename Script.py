''' 
#Prequisite#

#Template file (Sample)#

{
    "name" : "ARDTA.TEST.AR#TEST",
    "schema" : "ARDTA.TEST",
    "table" : "AR#TEST"
}

#List file (Sample)#

LIBRARY,TABLE
ARDTA.EAST,AR#BALANCE
ARDTA.WEST,AR#HISTORY

'''

import csv
import re

leng = 0
count = 1

#Calculate the number of lines in csv file
def generator(file_name):
    for row in open(file_name,"r"):
        yield row
for row in generator("lst.csv"):
    leng+=1

#overwriting the result file
with open("result.json","w") as res_obj:
    res_obj.write("")

#method to search and replace string
def replace_text(search_text,replace_text):
    with open("result.json","r+") as res_obj:
        f_obj = res_obj.read()
        f_obj = re.sub(search_text,replace_text,f_obj)
        res_obj.seek(0)
        res_obj.write(f_obj)
        res_obj.truncate()

#method to copy template to result file 
def copy_file():
    with open("template.json","r") as tp_obj, open("result.json","a") as res_obj:
        for line in tp_obj:
            res_obj.write(line)
        if count < 3:
            res_obj.write(",\n")

#Reading csv file row wise and slitting the elements delimited by ','
with open("lst.csv","r") as csvfile_obj,open("result.json","a") as resfile_obj:
    csvreader_obj = csv.reader(csvfile_obj)
    next(csvreader_obj)
    for row in csvreader_obj:
        count+=1
        copy_file()
        lib = row[0]
        tab = row[1]
        replace_text("ARDTA.TEST",lib)
        replace_text("AR#TEST",tab)