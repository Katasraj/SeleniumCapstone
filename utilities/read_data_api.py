import csv

class ReadData:
    def __init__(self, filepath):
        self.filepath = filepath

    def getCombinedData(self):
        combined_data = []
        with open(self.filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                combined_data.append((row['courseName'], float(row['price'])))
        return combined_data


r = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv")
print(r.getCombinedData())
