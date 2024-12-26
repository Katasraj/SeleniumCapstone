'''
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

# r = getCSVData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv")
# print(*r)
'''

import pandas as pd
import csv
from configfiles.location_filename import FileLocation

class ReadData:
    def __init__(self,filename):
        self.filename = filename

    def get_dropdownCourses(self):
        df = pd.read_csv(self.filename)
        DDcourseName = df['courseName'].values.tolist()
        return DDcourseName

    def getCSVData(self):
        df = pd.read_csv(self.filename)
        courseName = df['courseName'].values.tolist()
        return courseName

    def getCombinedData(self):
        combined_data = []
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                combined_data.append((row['courseName'], float(row['price'])))
        return combined_data

    def getCoursePrice(self):
        df = pd.read_csv(self.filename)
        #courseName = df['courseName'].values.tolist()
        prices = df['price'].values.tolist()
        return prices
        # cp = zip(courseName,Prices)
        # coursePrice = dict(cp)
        # return coursePrice


# c = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").getCSVData()
#d = ReadData(FileLocation().csv_location()[0]).getCombinedData()
# print(c)
#print(d)
# for courseName, price in d:
#     print(courseName,price)
#     print(f"Inserting course: {courseName} with price: {price}")
#d = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\configfiles\\drop_down_courses.csv").get_dropdownCourses()
#print(d)