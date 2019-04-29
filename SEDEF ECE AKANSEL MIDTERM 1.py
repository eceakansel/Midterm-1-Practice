#SEDEF ECE AKANSEL 2148500 GROUP 2
import numpy
import pandas
def processfile(filename):  #read file function for bought column and sum
    df = pandas.read_csv(filename, delim_whitespace=True)
    coffeetotal = numpy.asarray(df["Bought"]).sum()
    return coffeetotal
def processfile2(filename): #read file function for cost column and sum
    df2 = pandas.read_csv(filename,  delim_whitespace=True)
    costtotal = numpy.asarray(df2["Cost"]).sum()
    return costtotal
def processfile3(filename): #read file function for consumption column and sum
    df3 = pandas.read_csv(filename,  delim_whitespace=True)
    constotal = numpy.asarray(df3["Consumed"]).sum()
    return constotal
def processfile4(filename):  #read file function for unitprice column and sum
    df4 = pandas.read_csv(filename,  delim_whitespace=True)
    unitptotal = numpy.asarray(df4["UnitPrice"]).sum()
    return unitptotal
coffeetotal= processfile("C:\\Users\\e214850\\Desktop\\Coffee Consumption.txt")
costtotal= processfile2("C:\\Users\\e214850\\Desktop\\Coffee Consumption.txt")
constotal = processfile3("C:\\Users\\e214850\\Desktop\\Coffee Consumption.txt")
unitpttal = processfile4("C:\\Users\\e214850\\Desktop\\Coffee Consumption.txt")
rcosttotal = round(costtotal, 2)
averagecons = constotal / 14
raveragecons = round(averagecons, 2)
totalcost = round(unitpttal*averagecons,2)
print("Actual ordering method ends up ordering", coffeetotal , "grams of coffee at total cost of", rcosttotal)
print("A constant order level of", raveragecons, "results in ordering", constotal, "grams coffee at total cost of", totalcost)