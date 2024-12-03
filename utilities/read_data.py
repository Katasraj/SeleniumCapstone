import csv

def getCSVData(fileName):
    # Create an empty list to store rows
    rows = []

    #Open the CSV file
    dataFile = open(fileName,"r")

    #Create a CSV reader from CSV file
    reader = csv.reader(dataFile)

    #Skip the headers
    next(reader)

    #add rows from reader to list
    for row in reader:
        rows.extend(row)

    return rows

# r = getCSVData("F:\\PycharmProjects\\LetsKodeIt_2\\testdata.csv")
# print(*r)



