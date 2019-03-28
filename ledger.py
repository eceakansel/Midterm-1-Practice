import pandas
import numpy

def debitor(filename):
    df = pandas.read_csv(filename, sep = "\t", decimal = ".")
    array = numpy.asarray(df["Debit"])
    return array
def creditor(filename):
    df2 = pandas.read_csv(filename, sep = "\t", decimal = ".")
    array2 = numpy.asarray(df2["Credit"])
    return array2
def calculatedebit(entry):
    debit1 = 0
    if entry > 0:
        debit1 = entry
    return debit1
def calculatecredit(entry2):
    credit1 = 0
    if entry2 > 0:
        credit1 = entry2
    return credit1 
def totaldebit(darray):
    totaldbt = 0
    for entry in darray:
        debit = calculatedebit(entry)
        totaldbt = totaldbt + debit
    return totaldbt
def totalcredit(carray):
    totalcrdt = 0
    for entry2 in carray:
        credit = calculatecredit(entry2)
        totalcrdt = totalcrdt + credit
    return totalcrdt
darray = debitor("Tab Seperated Ledger.txt")
carray = creditor("Tab Seperated Ledger.txt")
debitt = totaldebit(darray)
credit = totalcredit(carray)
print("Total Credit is", credit)
print("Total Debit is", debitt)
print("Difference between debit and credit is", debitt-credit)