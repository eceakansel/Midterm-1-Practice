import pandas
import numpy

def processfileentry(filename):
    df = pandas.read_csv(filename, sep = "\t", decimal = ".")
    array = numpy.asarray(df["Entry"])
    return array
def processfileexit(filename):
    df2 = pandas.read_csv(filename, sep = "\t", decimal = ".")
    barray = numpy.asarray(df2["Exit"])
    return barray
def calculateenter(entry):
    enter = 0
    if entry > 0 :
        enter=entry
    return enter
def calculateexit(entry2):
    exit1 = 0
    if entry2 > 0 :
        exit1 = entry2
    return exit1
def totalenter(darray, sayı):
    totalenter = 0
    for entry in darray:
        enter = calculateenter(entry)
        totalenter = totalenter + enter
    avgenter = totalenter / sayı
    return avgenter
def totalexit(carray, sayı):
    totalexit = 0
    for entry2 in carray:
        exit2 = calculateexit(entry2)
        totalexit = totalexit + exit2
    avgexit = totalexit / sayı
    return avgexit
darray = processfileentry("employees.txt")
carray = processfileexit("employees.txt")
sayı = len(carray)
exit4 = totalexit(carray,sayı)
entry1  = totalenter(darray, sayı)
print("Average turnover is", exit4 - entry1)